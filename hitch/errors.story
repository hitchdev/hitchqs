If directory exists, abandon:
  about: |
    Output error message if a directory already
    exists where we were going to build.
  given:
    python version: 3.7.0
    files:
      hitch/key.py: |
        # Existing code
  steps:
  - quickstart:
      args: skeleton key
      exit code: 1
      will output: Directory 'hitch' already exists here, remove it to run quickstart
        again.
