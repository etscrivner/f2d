# Night 1, January 6, 2015

Began development tonight by getting together all of the Django interfaces. Then
rolled bootstraps default marketing template into something usable. Originally I
had planned to make a separate signup step where the user had to explicitly
agree to our Terms of Service (TOS) before being allowed to connect. I developed
this whole flow, which completely changed by the end. I'll come back to that in
due time.

By far the longest part of the development process was getting the SoundCloud
OAuth to work and using the Entity-Interactor pattern properly when persisting
and retrieving the appropriate user data.
