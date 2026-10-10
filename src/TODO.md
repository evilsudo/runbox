Phase 1 — Process creation

Foundation

Learn how to launch an executable, pass arguments, and collect its exit status using native OS interfaces.

Deliverable: A minimal process runner that launches a program and reports its result.
Phase 2 — Output handling

Pipes and file descriptors

Capture stdout and stderr separately, handle large outputs, and prevent pipe deadlocks.

Deliverable: Reliable output capture for short-running and high-output processes.
Phase 3 — Timeouts and cleanup

Lifecycle management

Implement deadlines, process termination, exit-status collection, and reliable cleanup when errors occur.

Deliverable: A runner that doesn't hang indefinitely or leak resources.
Phase 4 — Cross-platform support

POSIX and Windows

Build separate platform backends behind a common API. Use POSIX process interfaces on Linux/macOS and native Windows process APIs through ctypes.

Deliverable: Consistent behavior across supported operating systems.
Phase 5 — Testing and packaging

Release quality

Add unit tests, type hints, documentation, CI, and package metadata.

Deliverable: An installable Python library with documented platform limitations.

(chat gpt gave me ts but it's a good idea lowk)
