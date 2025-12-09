package app;

import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;

public class AppTest {
    @Test
    void music() { assertEquals("audio", App.route("Play music")); }

    @Test
    void phone() { assertEquals("phone", App.route("Call mom")); }

    @Test
    void nav()   { assertEquals("nav", App.route("Start route")); }

    @Test
    void empty() { assertEquals("empty", App.route("")); }
}
