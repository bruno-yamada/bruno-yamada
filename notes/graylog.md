
# Troubleshooting
check queued messages in System > Nodes
If not possible, check journal sizes:
du -sh /var/lib/graylog-server/journal/messagejournal-0
If possible, pause any trouble-causing input