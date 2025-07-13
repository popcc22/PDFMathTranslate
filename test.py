from pdf2zh import translate_stream

translate_stream(files=["doc.pdf"],
          service='deepseek',
          envs={"OPENAI_API_KEY":"sk-4af0d845c2264596bb6b03baa16d4267"}
          )