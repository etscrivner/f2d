# Software Design Overview

By: Eric Scrivner

This document is here to provide a brief explanation for some of the design
choices so future maintainers of the software can hopefully understand it.


## Entity-Interactor Pattern

The software has been designed to utilize the Entity-Interactor pattern as
detailed in this Bob Martin
[talk](http://confreaks.com/videos/759-rubymidwest2011-keynote-architecture-the-lost-years).

Why this design pattern?

So that should we need to switch databases or web frameworks or something else
in the future the software doesn't have to change significantly to support that.
This design pattern was invented with this kind of robustness as its target.

For this reason, please bare with what may seem like obtuse ways of doing
things. I can promise you that the decoupling achieved is a desirable result for
which the occassional roundabout approach should be borne.
