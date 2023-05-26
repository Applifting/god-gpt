## Whisper.cpp setup

Go to whisper.cpp module. 

Download the base.en model:

```bash
bash ./models/download-ggml-model.sh base.en
```

Now build the [main](examples/main) example and transcribe an audio file like this:

```bash
# build the main example
make

# transcribe an audio file to test everything works
./main -f samples/jfk.wav
```
