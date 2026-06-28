movies = (
    ("Interstellar", 2014, 8.7),
    ("Inception", 2010, 8.8),
    ("The Dark Knight", 2008, 9.0),
)

best = max(movies, key=lambda m: m[2])
avg  = sum(m[2] for m in movies) / len(movies)

print("All movies:")
for title, year, rating in movies:
    print(f"  {title} ({year}) — {rating}")

print(f"Highest rated: {best[0]} — {best[2]}")
print(f"Average rating: {avg:.2f}")