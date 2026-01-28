import { useState } from "react";
import { api } from "../api";

export default function UploadForm() {
  const [pdf, setPdf] = useState<File | null>(null);
  const [jd, setJd] = useState("");
  const [loading, setLoading] = useState(false);

  const submit = async () => {
    if (!pdf || !jd) {
      alert("Please upload a PDF and enter a JD URL");
      return;
    }

    const form = new FormData();
    form.append("pdf", pdf);
    form.append("jd_url", jd);

    try {
      setLoading(true);
      await api.post("/api/generate", form, {
        headers: { "Content-Type": "multipart/form-data" }
      });
      alert("Resume Generated!");
    } catch (err) {
      console.error(err);
      alert("Failed to generate resume");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100">
      <div className="bg-white p-6 rounded shadow space-y-4 w-full max-w-md">
        <input
          type="file"
          accept="application/pdf"
          onChange={(e) => setPdf(e.target.files?.[0] || null)}
          className="block w-full"
        />

        <input
          className="border p-2 w-full"
          placeholder="Job Description URL"
          value={jd}
          onChange={(e) => setJd(e.target.value)}
        />

        <button
          onClick={submit}
          disabled={loading}
          className="bg-black text-white px-4 py-2 rounded w-full disabled:opacity-50"
        >
          {loading ? "Generating..." : "Generate Resume"}
        </button>
      </div>
    </div>
  );
}
