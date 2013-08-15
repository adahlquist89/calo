#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "calo_social.settings")
    from django.core.management import execute_from_command_line
    import calo_social.startup as startup
    startup.run()
    execute_from_command_line(sys.argv)
