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


Tutorial not found:
  given:
    python version: 3.7.0
  steps:
  - quickstart:
      args: demo nonexistent
      exit code: 1
      will output: demo 'nonexistent' does not exist.

#Too many arguments:
