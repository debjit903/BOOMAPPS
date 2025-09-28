from http.server import SimpleHTTPRequestHandler, HTTPServer
import logging
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

PORT = 8000

# Custom Logging Handler
class LoggingHandler(SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        client_ip = self.client_address[0]
        time = self.log_date_time_string()
        msg = format % args

        log_line = f"{Fore.CYAN}{Style.RESET_ALL} - " \
                   f"[{Fore.YELLOW}{time}{Style.RESET_ALL}] " \
                   f"{Fore.GREEN}{msg}{Style.RESET_ALL}"

        logging.info(log_line)

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(message)s",   # শুধু কাস্টম মেসেজ দেখাবে
        handlers=[logging.StreamHandler()]
    )

    server = HTTPServer(("0.0.0.0", PORT), LoggingHandler)
    print(f"{Fore.MAGENTA}Serving at http://127.0.0.1:{PORT}{Style.RESET_ALL}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}Shutting down server...{Style.RESET_ALL}")
        server.server_close()