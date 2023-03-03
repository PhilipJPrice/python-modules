def get_pages(*links):
    """Arbitrary number of arguments for links"""
    for link in links:
        # Download the link with urllib
        print(link)
