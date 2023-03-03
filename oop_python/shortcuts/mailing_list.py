from collections import defaultdict

class MailingList:
    """Manage groups of e-mail addresses for sending e-mails."""

    def __init__(self):
        self.data_file = data_file
        self.email_map = defaultdict(set)

    def add_to_group(self, email, group):
        self.email_map[email].add(group)

    def send_mailing(
        self, subject, message, from_addr, *groups, headers=None):
        emails = self.emails_in_groups(*groups)
        send_email(subject, message, from_addr, *emails, headers=headers)

    def save(self):
        with open(self.data_file, "w") as file:
            for email, groups in self.email_map.items():
                file.write("{} {}\n".format(email, ",".join(groups)))

    def load(self):
        self.email_map = defaultdict(set)
        with suppress(IOError):
            with open(self.data_file) as file:
                for line in file:
                    email, groups = line.strip().split(" ")
                    groups = set(groups.split(","))
                    self.email_map[email] = groups

    def __enter__(self):
        self.load()
        return self

    def __exit__(self, type, value, tb):
        self.save()
