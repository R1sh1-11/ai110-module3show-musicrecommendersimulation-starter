# Reflection: Music Recommender Simulation

## Profile Comparisons

### Happy Pop Fan vs. Chill Lofi Listener

These two profiles produced completely different top 5 lists with zero overlap. The Pop Fan got upbeat, high-energy tracks (Sunrise City, Gym Hero) while the Lofi Listener got mellow, acoustic tracks (Midnight Coding, Library Rain). This makes sense because the profiles differ on every single preference: genre, mood, energy, and acoustic preference. It shows the system can clearly distinguish between very different types of listeners.

### Happy Pop Fan vs. Intense Rock Lover

Interestingly, Gym Hero appeared in both lists: #2 for the Pop Fan and #2 for the Rock Lover. For the Pop Fan it matched on genre (pop), and for the Rock Lover it matched on mood (intense). This shows how a high-energy song can appeal to different users for completely different reasons. Sunrise City appeared in the Pop Fan's list at #1 but only at #5 for the Rock Lover, where it had no genre or mood match: just decent energy.

### Intense Rock Lover vs. Sad But Energetic (Edge Case)

Both profiles want high energy, but the Rock Lover wants "intense" mood while the Sad profile wants "melancholy." Storm Runner dominated for the Rock Lover (genre + mood + energy = 3.99) but did not even appear in the Sad profile's top 5 because it had no genre or mood match. Instead, the Sad profile's list was mostly driven by pop genre matching and raw energy scores. The only melancholy song, Autumn Letters, ranked #3 for the Sad profile but with a low score (1.35) because its energy (0.30) was far from the target (0.95). This shows the system struggles when mood and energy conflict.

### Chill Lofi Listener vs. Quiet Classical Fan (Edge Case)

Both profiles want low energy and acoustic music, but they differ on genre and mood. The Lofi Listener got lofi tracks while the Classical Fan got classical and jazz tracks. Despite the similar "vibe," there was only one shared song in both top 5 lists. Library Rain appeared at #2 for the Lofi Listener and #5 for the Classical Fan. The acoustic bonus helped surface mellow tracks for both profiles, but genre preference kept their lists mostly separate. This demonstrates that the system can distinguish between users who want a similar feel but from different musical traditions.

### Normal Profiles vs. Edge Cases

The three normal profiles all had a clear #1 song that scored well above the rest (3.98, 4.48, 3.99). The edge cases were more chaotic, the Sad But Energetic profile had a much flatter distribution of scores because no song matched all its conflicting preferences well. The Quiet Classical Fan was the exception, scoring Starlit Waltz at 4.50, because the catalog happened to have a perfect match. This shows that the system's confidence depends heavily on whether the catalog contains songs that align with the full set of preferences.

## What I Learned

The most important takeaway is that recommendation systems are really just scoring functions applied at scale. The math is simple: addition, subtraction, comparison but the choices about what to score and how much weight to give each factor have huge consequences for what users see. A small change like doubling the energy weight completely reshuffled the rankings.

I also learned that bias can sneak in through the data, not just the algorithm. Even though my scoring logic treats all genres equally, the fact that some genres only have one song in the catalog means those users get less variety. In a real system with millions of songs, this might show up as popular genres getting more representation simply because there is more data available for them.
