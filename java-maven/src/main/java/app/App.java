package app;

/**
 * Utility class that routes free-form voice commands
 * to a target subsystem id.
 */
public final class App {

  private App() {
    // utility class
  }

  /**
   * Route a command string to a subsystem id.
   *
   * @param cmd the command text
   * @return "audio", "phone", "nav", "empty" or "unknown"
   */
  public static String route(final String cmd) {
    if (cmd == null || cmd.trim().isEmpty()) {
      return "empty";
    }

    final String s = cmd.toLowerCase();

    if (s.contains("music")) {
      return "audio";
    }

    if (s.contains("call")) {
      return "phone";
    }

    if (s.contains("route") || s.contains("nav")) {
      return "nav";
    }

    return "unknown";
  }
}

