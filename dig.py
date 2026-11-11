import subprocess


def dig(domain):
    """
    Perform a DNS lookup for the given domain using an external API.

    Args:
        domain (str): The domain name to look up.  """

    try:
        # Use the 'dig' command to perform the DNS lookup
        result = subprocess.run(['dig', domain], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"An error occurred while performing the DNS lookup: {e}"


if __name__ == "__main__":
    domain = input("Enter a domain to look up: ")
    result = dig(domain)
    print(result)
