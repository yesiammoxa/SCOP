from modules import instagram, tiktok, twitter, whatsapp
from core.graph import SocialGraph
from core.correlate import correlate
from core.report import save_report

def print_banner():
    try:
        with open("banner.txt", "r", encoding="utf-8") as f:
            print(f.read())
    except:
        pass

def main():
    print_banner()

    username = input("Username: ").strip()
    phone = input("Phone (optional): ").strip() or None

    results = []

    results.append(instagram.scan(username))
    results.append(tiktok.scan(username))
    results.append(twitter.scan(username))

    if phone:
        results.append(whatsapp.scan(phone))

    graph = SocialGraph()

    for r in results:
        if not r:
            continue
        user = r.get("username")

        for f in r.get("followers", []):
            graph.add_relation(user, f)

        for f in r.get("following", []):
            graph.add_relation(user, f)

    output = {
        "target": username,
        "accounts": results,
        "graph": graph.stats(),
        "correlation": correlate(results)
    }

    save_report(output)
    print("[+] Done. Results saved.")

if __name__ == "__main__":
    main()
