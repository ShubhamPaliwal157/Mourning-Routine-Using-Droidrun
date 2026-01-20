"""
Morning Routine Automation using DroidRun

Trigger:
    User turns off the morning alarm

Workflow:
    1. Enable Wi-Fi
    2. Enable Mobile Data
    3. Disable Do Not Disturb / Mute
    4. Open Spotify and play Liked Songs
    5. Open Weather application
"""

from droidrun import (
    EventTrigger,
    SystemControl,
    AppControl,
    MediaControl,
    Routine
)

def morning_routine():
    routine = Routine(name="Morning Routine Automation")

    # Step 1: Enable connectivity
    routine.add_step(SystemControl.enable_wifi())
    routine.add_step(SystemControl.enable_mobile_data())

    # Step 2: Ensure sound is enabled
    routine.add_step(SystemControl.disable_do_not_disturb())
    routine.add_step(SystemControl.set_ringer_mode("normal"))

    # Step 3: Start music
    routine.add_step(AppControl.open_app(package_name="com.spotify.music"))
    routine.add_step(
        MediaControl.play_playlist(
            app="spotify",
            playlist_name="Liked Songs"
        )
    )

    # Step 4: Open weather app
    routine.add_step(
        AppControl.open_app(package_name="com.android.weather")
    )

    return routine


if __name__ == "__main__":
    # Triggered when the user dismisses the alarm
    alarm_dismissed = EventTrigger.on_alarm_dismiss()

    alarm_dismissed.bind(
        action=morning_routine()
    )

    alarm_dismissed.start_listening()
