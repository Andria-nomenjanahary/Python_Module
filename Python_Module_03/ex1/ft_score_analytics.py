#!/usr/bin/env python3
import sys


def score_analytics() -> None:
    i = 1
    if len(sys.argv) == 1:
        print(
            "No scores provided. Usage: python3 "
            "ft_score_analytics.py <score1> <score2> ..."
        )
        return
    valid_arg: list[str] = []
    while i < len(sys.argv):
        try:
            int(sys.argv[i])
            valid_arg += [sys.argv[i]]
        except ValueError:
            print(f"Invalid parameter: '{sys.argv[i]}'")
        except Exception as e:
            print(f"Error: {e}")
        i += 1
    if len(valid_arg) == 0:
        print(
            "No scores provided. Usage: python3 "
            "ft_score_analytics.py <score1> <score2> ..."
        )
    else:
        scores: list[int] = []
        for item in valid_arg:
            scores = scores + [int(item)]
        print(f"Scores processed: {scores}")
        print(f"Total players: {len(scores)}")
        print(f"Total score: {sum(scores)}")
        print(f"Average score: {sum(scores) / len(scores):.1f}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}\n")
    return


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    score_analytics()
