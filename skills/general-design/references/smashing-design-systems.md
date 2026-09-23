# design-systems-smashing-ebooks

> **Manba**: C:\Users\CUBO\Desktop\Files\books\Umumiy dizayn\design-systems-smashing-ebooks.pdf
> **Jami sahifalar**: 284

---

### Sahifa 1

./AOO/.../AA/ x x x Design Systems A practical guide to creating design languages for digital products. by Alla Kholmatova x • / AX X A • • / ox x x x

### Sahifa 2

x Design Systems A practical guide to creating design languages for digital products. xx by Alla Kholmatova A x x x / ox / ox x x x x o o • •

### Sahifa 4

Imprint
Published 2017 by Smashing Media AG, Freiburg, Germany.
All Rights Reserved.
ISBN (ePUB): 978-3-945749-60-9
Cover Design: Espen Brunborg.
Proofreading: Owen Gregory.
eBook production: Cosima Mielke.
Print layout: Markus Seyfferth.
Design Systems was written by Alla Kholmatova and reviewed by Karen McGrane and Jeremy 
Keith.
Please send errors to: errata@smashingmagazine.com

### Sahifa 5

To Alyona

### Sahifa 6

Table Of Contents
Imprint
About The Author
Foreword
Introduction
PART 1: FOUNDATIONS
1. Design Systems
2. Design Principles
3. Functional Patterns
4. Perceptual Patterns
5. Shared Language
Summary
PART 2: PROCESS
6. Parameters Of Your System
7. Planning And Practicalities
8. Systemizing Functional Patterns
9. Systemizing Perceptual Patterns

### Sahifa 7

10. Pattern Libraries
Conclusion
Copyright Information

### Sahifa 8

About The Author
Alla Kholmatova is a UX and interaction designer with a nine-year experience of 
working on the web, for a range of products and companies. Most recently she was a 
senior product designer at an open education platform, FutureLearn.
She’s particularly interested in design systems, language, and collaborative ways of 
working. In the last two years this interest has led her to spend a huge amount of 
time working on and researching the subject. She’s been sharing her insights with 
people through articles, workshops, and projects. Alla contributes to design 
publications, such as A List Apart, and speaks at conferences around the world.

### Sahifa 9

About The Reviewers
Karen McGrane has helped businesses create better digital products through the 
power of user experience design and content strategy for the past twenty years. She 
is Managing Partner at Bond Art + Science, a UX consultancy she founded in 2006 
and formerly VP and National Lead for User Experience at Razorfish. Karen teaches 
Design Management in the MFA in Interaction Design program at the School of 
Visual Arts in Manhattan. She co-hosts A Responsive Web Design Podcast with 
Ethan Marcotte, and her first book, Content Strategy for Mobile , was published in 
2012 by A Book Apart.
Jeremy Keith is co-founder and technical director at Clearleft, a digital design studio 
based in Brighton, England. When he’s not making websites, he talks at conferences 
about making websites. Sometimes he even writes books about making websites, 
like the web book at ResilientWebDesign.com that you can have for free. But he 
mostly spends his time goofing off on the internet, documenting his time-wasting on 
his website adactio.com where he has been writing for over fifteen years.
—
1.
http://smashed.by/contentmob
1

### Sahifa 10

Foreword
If you have a moment, look up the work of artist Emily Garfield. She creates 
exquisite, intricately detailed maps in watercolor — each of them stunning, and each 
of them depicting a place that doesn’t exist. Instead of depicting a city’s real, actual 
landscape, she begins by creating a single, complex pattern — a knotted road or 
twisty river, or a compact grid of city blocks — and repeating it. Garfield iterates on 
that pattern, changing it slightly each time, spiraling out until her not-map is 
finished. As a result, her art has a generative, fractal-like quality: it’s built from 
patterns, yes, but feels part of a cohesive whole.
In fact, Garfield once said, “I describe my process as growing the drawing.” While 
reading this wonderful book by Alla Kholmatova — this book that you’re about to 
read — I thought about that line a lot. Maybe you will, too.
In recent years, web designers have started embracing more modular, pattern-driven 
design practices. And with good reason: we’re being asked to create compelling 
experiences for more screens, more devices, more places, more people than ever 
before. As a result, we’ve started to break our interfaces down into tiny, reusable 
modules, and begun using those patterns to build products, features, and interfaces 
more quickly than ever before.
But by themselves, design patterns aren’t enough. They need to live within a larger 
process, one that ensures these little interface modules feel unified, cohesive, 
connected. Part of a whole. In other words, they need a design system to thrive — 
and that’s where Alla’s book comes in.
In these pages, Alla shows us precisely how to create systems to support our digital 
designs. With clear writing, case studies, and detailed examples, Alla shows us how 
to establish a common, shared language among our teams, which allows us to more 
effectively collaborate; she’ll tell stories of how different organizations have created 
their design systems, and put them into practice; and she’ll discuss different models

### Sahifa 11

for evolving these systems over time.
In other words, this isn’t just a book. Alla has drawn a clear, bright map for us, one 
that outlines a more sustainable model for digital design. And if we walk the paths 
she’s drawn for us, we’ll learn to grow better design systems — and with them, 
better designs.
— Ethan Marcotte

### Sahifa 12

Introduction

### Sahifa 13

What This Book Is About
As the web continues to change rapidly and become more complex, thinking of it in 
terms of static pages has become untenable, and many of us have started to approach 
design in a more systematic way.
And yet not all design systems are equally effective. Some can generate coherent 
user experiences, others produce confusing patchwork designs. Some inspire teams 
to contribute to them, others are neglected. Some get better with time, more cohesive 
and better functioning; others get worse, becoming bloated and cumbersome.
What are the key qualities of a well-functioning, enduring design system? This 
question intrigued me so much I spent a huge amount of time researching and 
thinking about it. My research and thoughts provide the basis of this book. Drawing 
on the experience of companies of various sizes and approaches to design systems, I 
set out to identify what makes an effective system that can empower teams to create 
great digital products. Throughout the book I’ll share an approach that helps me 
every day with my work. I hope this will help with your work, too.

### Sahifa 14

Who This Book Is For
This book is aimed mainly at small and medium-sized product teams trying to 
integrate design systems thinking into their organization’s culture. Everyone in the 
product team could benefit from reading this book, but particularly visual and 
interaction designers, UX practitioners and front-end developers.

### Sahifa 15

Scope Of The Book
This book presents a perspective on design systems based on my experience as an 
interaction and visual designer. I don’t touch on other related areas, such as 
information architecture, content strategy or design research. Equally, this is not a 
technical book. You won’t find any code samples or in-depth analysis of 
development tools and techniques, although there will be plenty of discussion 
directly related to front-end practices.
This is a design book, but it isn’t about what to design. Neither is it an attempt to 
create a comprehensive guide to designing digital products. It is about how to 
approach your design process in a more systematic way, and ensure your design 
system helps to achieve the purpose of your product and fits with the culture of your 
team.
1

### Sahifa 16

How This Book Is Organized
The book has two parts.
PART 1: FOUNDATIONS
In the first part we’ll talk about the foundations of a design system — patterns and 
practices. Design patterns are repeatable, reusable parts of the interface, from the 
concrete and functional (like buttons and text fields) to the more descriptive (like 
iconography styles, colors and typography). Patterns interconnect, and together they 
form the language of your product’s interface. Shared practices are how we choose 
to create, capture, share and use those patterns — by following a set of principles, or 
by keeping a pattern library.
PART 2: PROCESS
A design system cannot be built overnight — it evolves gradually with your product. 
But there are certain principles and practices that we can follow to make sure the 
system develops in the right direction and provide us some degree of control over it. 
The second part of the book focuses on practical steps and techniques to establish 
and maintain a design system, including: planning the work; conducting an interface 
inventory; setting up a pattern library; creating, documenting, evolving and 
maintaining design patterns.

### Sahifa 17

Terminology
Before we dive into the topic, let’s establish the terms we’ll use throughout the book.
Pattern or design pattern
I use the word pattern to refer to any repeating, reusable parts of the interface (such 
as buttons, text fields, iconography styles, colors and typography, repeating user 
flows, interactive behaviors) that can be applied and repurposed to solve a specific 
design problem, meet a user need, or evoke an emotion. Throughout the book, I 
distinguish between functional patterns related to behaviors, and perceptual patterns 
related to brand and aesthetics.
Functional patterns or modules
These terms are used interchangeably throughout the book, to refer to tangible 
building blocks of the interface, such as a button, a header, a form element, a menu.
Perceptual patterns or styles
These are more descriptive and less tangible design patterns, such as iconography 
styles or colors and typography, typically used to create a certain kind of aesthetic 
and strengthen an emotional connection with a product.
Pattern language or design language
A set of interconnected, shareable design patterns forms the language of your 
product’s interface. A pattern language combines functional and perceptual patterns, 
as well as platform-specific patterns (such as the hamburger menu), domain patterns 
(such as modules specific to an e-commerce site, or finance software, or a social 
app), UX and persuasive patterns, and many other types meshed together in an 
interface for a specific product.
Design system or system

### Sahifa 18

There isn’t a standard definition of “design system” within the web community, and 
people use the term in different ways — sometimes interchangeably with “style 
guides” and “pattern libraries.” In this book, by design system I mean a set of 
connected patterns and shared practices, coherently organized to serve the purposes 
of a digital product.
Pattern library and style guide
A pattern library is a tool to capture, collect and share design patterns and guidelines 
for their usage. Creating a pattern library is an example of a (good) design practice. 
Traditionally, a style guide focuses on styles, such as such as iconography styles, 
colors and typography, while a pattern library includes a broader set of patterns.

### Sahifa 19

Design System Insights
The book is based on practical insights from real-world products. Most of them are 
drawn from my experience of working at FutureLearn , a medium-sized open 
education company in London. During my three years working there as a designer, I 
have had an opportunity to observe and influence how a design system evolves, from 
initial concepts to a mature system .
To have more depth and diversity in the research, I also closely followed five other 
companies of different sizes and approaches to design systems: Airbnb, Atlassian, 
Eurostar, Sipgate, and TED. Over the course of 18 months I’ve been interviewing 
members of their teams, to understand directly from the team, the challenges they 
face as their systems evolve. The companies who have kindly agreed to share their 
insights are as follows.
AIRBNB
When interviewed in August 2016, Roy Stanfield (Principal Interaction Designer) 
gave me plenty of detail about the Design Language System at Airbnb.The 
distinguishing aspect of DLS is its strictness. Patterns are specified and used 
precisely and rules are followed closely. The team has placed a number of practices 
and tools in place to achieve that. They still have some challenges with adoption, 
speed of integrating new patterns, and with keeping art direction and engineering in 
sync.
ATLASSIAN
Jürgen Spangl (Head of Design), James Bryant (Lead Designer), and Kevin Coffey 
2
3
4
5
6

### Sahifa 20

(Design Manager) shared their perspectives on ADG (Atlassian Design Guidelines ) 
in November 2016. While there’s a dedicated team who curates the patterns, they 
also have an open source model for contributions. Everyone in the company is not 
only allowed, but actively encouraged to contribute to the system. The challenge 
with this model is to find a balance between giving people enough freedom to 
contribute, yet making sure the system stays managed and curated.
EUROSTAR
Dan Jackson (Solutions Architect) was very forthcoming in August and September 
2016 and in March 2017 about what they’ve been doing at Eurostar. At the time of 
writing, the team was in the process of building their first pattern library . They 
initially experienced some challenges, particularly with prioritizing the project and 
encouraging everyone on the team to contribute. After a year, they were given the 
resources to allocate a dedicated team, which is now leading the work on the system.
SIPGATE
Tobias Ritterbach (Experience Owner) and Mathias Wegener (Web Developer) both 
gave me a lot of insight into their work in August 2016 and November 2016. The 
Sipgate pattern library was established in 2015, but after a year the team found that 
there were too many patterns, mainly due to a lack of communication between the 
product teams. More recently, they were in the process of working on a new pattern 
library, with a goal to unify the design language across several product websites.
TED
Michael McWatters (UX Architect), Aaron Weyenberg (UX Lead) and Joe Bartlett 
(Front-End Developer) all provided input into discussions in August and September 
2016. Among the many people who support TED.com, a small handful of UX 
7
8
9
10
11
12

### Sahifa 21

practitioners and front-end developers are responsible for design system decisions. 
The team has a deep shared knowledge of their patterns, which are documented in a 
simple way . So far they haven’t felt a need to establish a comprehensive pattern 
library.
13

### Sahifa 22

Acknowledgements
I want to thank everyone at FutureLearn for their support of this book, in particular: 
Lucy Blackwell, for reviewing the early drafts and for guiding and inspiring me to 
do my best work; Mike Sharples, for the thought-provoking feedback on the early 
draft and for challenging me; Gabor Vajda, for helping me to shape many of the 
ideas described in the book; Jusna Begum, for bringing some order and structure to 
my chaotic thoughts; and Sam McTaggart, Dovile Sandaite, Kieran McCann, Storm 
MacSporran, Katie Coleman, Nicky Thompson, James Mockett, Chris Lowis and 
Matt Walton, for taking the time to listen and for sharing their feedback.
Huge thanks to the Smashing crew and everyone who helped me shape this book and 
make it happen. A special thanks to Karen McGrane, Jeremy Keith and Vitaly 
Friedman, for the thoughtful and constructive feedback which made this book so 
much better; Owen Gregory, for editing the book; to Ethan Marcotte for the 
foreword; and Espen Brunborg for the beautiful cover design.
I would particularly like to thank the many people who kindly agreed to share their 
experiences and perspectives, many of which contributed to the material in the book: 
the teams mentioned in Design Systems Insights, as well as Sarah Drasner, Laura 
Elizabeth, Matt Bond, Trent Walton, and Geri Coady, and Joel Burges, Michal 
Paraschidis, Heydon Pickering, Léonie Watson, Bethany Sonefeld and Chris 
Dhanaraj (IBM), Amy Thibodeau (Shopify), and Joe Preston (Intuit).
Finally, I want to thank my family: my husband, Hakan, and my little daughter, 
Alyona, for the patience and understanding they gave me in the 18 months it took to 
reach a final draft. Writing a book while having a full-time job was an enormous 
amount of work and it would have been impossible without my husband’s support. 
I’m sorry, Alyona, for all the times I couldn’t play with you because I was busy

### Sahifa 23

working. I love you and I promise to make up for it!
—
1.
For that I recommend About Face: The Essentials of Interaction Design by Alan Cooper; 
Lean UX: Applying Lean Principles to Improve User Experience by Jeff Gothelf and Josh 
Seiden; and Designing for the Digital Age: How to Create Human-Centered Products and 
Services by Kim Goodwin.
2.
https://www.futurelearn.com/
3.
https://www.futurelearn.com/pattern-library
4.
https://www.airbnb.co.uk/
5.
http://smashed.by/airbnblanguage
6.
https://www.atlassian.com/
7.
https://atlassian.design/
8.
http://www.eurostar.com/
9.
https://style.eurostar.com/
10. https://www.sipgate.de/
11. https://design.sipgateteam.de/
12. http://www.ted.com/
13. http://ted.com/swatch

### Sahifa 24

Part 1: Foundations

### Sahifa 25

CHAPTER 1
Design Systems
There isn’t a standard definition of “design system” within the web community and 
people use the term in different ways. In this chapter, we’ll define what a design 
system is and what it consists of.
A design system is a set of interconnected patterns and shared practices coherently 
organized to serve the purpose of a digital product. Patterns are the repeating 
elements that we combine to create an interface: things like user flows, interactions, 
buttons, text fields, icons, colors, typography, microcopy. Practices are how we 
choose to create, capture, share and use those patterns, particularly when working in 
a team.
Take a look at these two screens of unrelated products. One is from Thomson 
Reuters Eikon, a trading and market analysis application; the other is from 
FutureLearn, an open education social learning site.
A screen from Thomson Reuters Eikon (left) and a screen from FutureLearn (right).
In each example the patterns work together to achieve different purposes. For 
Thomson Reuters, it’s about handling data, utility, quick scanning and multitasking; 
for FutureLearn, it’s about thoughtful reading, informal learning, reflection and 
connecting with like-minded people. The purpose of the product shapes the design

### Sahifa 26

patterns it adopts.
The Thomson Reuters layout is panel- and widget-based, to allow users to multitask. 
The design is dense, fitting large amounts of information on the screen. Density is 
achieved through tight spacing, compact controls, flexible layouts and typographic 
choices, such as a condensed typeface and relatively small headings. On the other 
hand, the FutureLearn layout is much more spacious. Each screen is typically 
focused on a single task, such as reading an article, engaging in a discussion, or 
completing an interactive exercise. The layout here is mostly a single column; 
there’s high-contrast typography with large headings, chunky controls, and generous 
white space.
The choice of design patterns is influenced by many factors. Some of them come 
from the domain the product belongs to, and from its core functionality: those are 
functional patterns. To use trading and market analysis software, for instance, you’d 
need to be accustomed to task bars, data fields and grids, charts and data 
visualization tools. For an online learning site, it could be articles, videos, discussion 
threads, progress indicators and interactive activities. An e-commerce site would 
most likely include a product display, list filters, shopping cart and a checkout.
The ethos of a product (or the brand, depending on your definition of a brand) also 
forms patterns which together shape how a product is perceived; throughout this 
book I’ll refer to them as perceptual patterns. By that I mean things like tone of 
voice, typography and color choices, iconography styles, spacing and layout, specific 
shapes, interactions, animations, and sounds. Without perceptual patterns you 
wouldn’t feel that much difference between products from within the same domain, 
which have similar functionality.
1

### Sahifa 27

Although HipChat and Slack have similar purposes and functionality, they feel quite different, 
largely due to how brand is expressed throughout their interfaces.
Patterns are also shaped by platform conventions. A product can feel distinctly web-
y or distinctly app-y because of a platform-specific design language. An iOS 
application for a product can behave and feel entirely different from its Android 
equivalent.
There are many kinds of patterns at play when it comes to creating a digital product. 
That’s why design is hard. Patterns need to interact, connect, yet still work 
seamlessly together. Let’s take a closer look at them.

### Sahifa 28

Design Patterns
The idea of design patterns was introduced by the architect Christopher Alexander in 
his seminal books, The Timeless Way of Building and A Pattern Language. One 
question that runs through the books is why some places feel so alive and great to be 
in, while others feel dull and lifeless. According to Alexander, the way places and 
buildings make us feel is not due to subjective emotions merely. It’s a result of 
certain tangible and specific patterns. Even ordinary people can learn and use them 
to create humane architecture.
A pattern is a recurring, reusable solution that can be applied to solve a design 
problem.
“Each pattern describes a problem that occurs over and over again in 
our environment, and then describes the core of the solution to that 
problem.”
— Christopher Alexander, A Pattern Language
A Pattern Language contains 253 architectural design patterns, starting from the 
larger ones, such as a layout of a city and road systems, down to the smallest ones, 
such as lighting and furniture in a family house.
Similarly, when creating interfaces we use design patterns to solve common 
problems: we use tabs to separate content into sections and indicate which option is 
currently selected; we use a dropdown to display a list of options at the user’s

### Sahifa 29

request.
Some of the patterns from Bootstrap, a front-end framework for developing responsive websites.
We use patterns to offer feedback, to show how many steps are left in a process, to 
allow people interact with each other, to view and select items. Design patterns can 
intrigue and encourage, make tasks easier, create a sense of achievement or an 
illusion of control.
2

### Sahifa 30

Example of persuasive pattern “recognition over recall” on UI Patterns .
Most of the design patterns are established and familiar. They make use of people’s 
mental models and allow design to be understood intuitively. Entirely new patterns 
require users to learn and adopt them first — they are relatively rare. What makes a 
product distinct from its competitors is not the novelty of patterns it uses, but how 
those patterns are executed and applied, and how they interconnect to achieve a 
design purpose. A set of interconnected patterns forms the design language of your 
product’s interface.
A design language emerges as we work on a product. We don’t always know what 
this language is. Sometimes, effective and interesting designs are based on intuition, 
and we struggle to articulate exactly how and why they work. Designers and 
developers might know it instinctively, but intuition is not always reliable or 
3
4

### Sahifa 31

scalable. In his article “Researching Design Systems,” designer Dan Mall noted that 
one of the main goals of a design system is “extending creative direction.” If you 
need to get a group of people to follow a creative direction consistently, reliably and 
coherently, patterns need to be articulated and shared.
When you articulate your design language it becomes actionable and reproducible. 
You start approaching design with a system in mind. For example, instead of 
discussing how to tweak an item to make it stand out more, you can have a suite of 
promotional patterns, each one targeted to achieve a different level of visual 
prominence. The visual loudness guide by Tom Osborne is an example of how 
buttons and links can be approached systematically. Instead of listing them 
individually, they are presented as a suite, each one having a different “volume” 
corresponding to its intended visual prominence.
7
6

### Sahifa 32

The visual loudness guide by Tom Osborne.
Articulating your language allows you to gain more control over the system. Rather 
than making small tweaks, you can affect it in much more profound ways. If you 
discover a small design change which made a positive impact on user experience, 
you can apply it to the pattern across the system rather than to one place. Instead of 
spending hours on designing a dropdown, you can spend that time with the users and 
domain experts, finding out if a dropdown is needed in the first place. When the 
design language is shared knowledge, you can stop focusing on the patterns

### Sahifa 33

themselves and instead focus more on the user.
Throughout the book we’ll talk a lot about articulating, sharing and documenting a 
pattern language for digital products. In particular, we’ll look at two types of design 
patterns: functional and perceptual. Functional patterns are represented as concrete 
modules of the interface, such as a button, a header, a form element, a menu. 
Perceptual patterns are descriptive styles that express and communicate the 
personality of the product visually, such as color and typography, iconography, 
shapes and animations.
To extend the analogy with language, functional patterns are a bit like nouns or verbs 
— they are concrete, actionable parts of the interface; whereas perceptual patterns 
are similar to adjectives — they are descriptive. For example, a button is a module 
with a clear function: allow users to submit an action. But the typographic style in 
the label of the button, its shape, background color, padding, interactive states and 
transitions are not modules. They are styles; they describe what kind of button it is. 
From a front-end perspective, modules always have a basis in HTML, and perceptual 
patterns are typically CSS properties.
A design system contains many other kinds of patterns: user flows (such as 
completion of forms with errors and success messages), domain-oriented design 
patterns (like learning patterns for EdTech systems, and e-commerce patterns), and 
persuasive UX patterns. The focus of this book is on the functional and perceptual 
patterns as the core building blocks of a design system.
But, of course, what matters is not only the patterns themselves, but how they are 
evolved, shared, connected and used.

### Sahifa 34

Shared Language
Language is fundamental to collaboration. If you work in a team, your design 
language needs to be shared among the people involved in the creation of the 
product. Without a shared language, a group of people can’t create effectively 
together — each person will have a different mental model of what they’re trying to 
achieve. Let’s return to the button example. Even such a basic unit of the interface 
can have different meanings. What exactly is a button? An outlined area that you can 
click on? An interactive element on a page that links somewhere? A form element 
that allows users to submit some data?
In her book How to Make Sense of Any Mess, Abby Covert suggests that a shared 
language should be established before you think about interfaces, by discussing, 
vetting and documenting our language decisions. This idea could be applied to 
describing high-level concepts as well as the day-to-day language we use to talk 
about design decisions. Having a shared language would mean that we have the same 
approach to naming interface elements and defining design patterns, or that the same 
names are used in design files and front-end architecture.
Even that might not be enough. Sometimes, people in a group think they have 
reached a mutual understanding because they share the same vocabulary and use it 
expressively, but they still retain fundamental differences in understanding. For 
example, after a year of using the term “Scenario” as a key concept in a project, you 
might discover that different people are interpreting it in entirely different ways. It’s 
not only about developing a shared language — we need also to develop a shared use 
of language. It’s not enough to have a shared understanding of the term button. 
People must also know why and how to use a button, in what contexts, and the 
purpose a button can serve.

### Sahifa 35

Suppose we use an element called “Sequence” in the interface. By presenting it as 
“Sequence” we aim to communicate to users that the steps should be looked at in a 
specific order.
Example of “Sequence” module.
Ideally, everyone involved in the creation of the product should know what this 
element is: its name and purpose, why it’s been designed that way, and how and 
when it should be used. The stronger this shared knowledge is, the higher the 
chances that it will be used appropriately. Designers and front-end developers should 
have this knowledge, but it helps if people from other disciplines (content, 
marketing, product management) have some idea too.
It should be known to everyone as “Sequence,” not “Wizard control” or “Fancy 
bubbles.” If designers refer to it as “Fancy bubbles,” developers call it “Wizard 
control” and users interpret it as set of optional tabs, then you know your language 
doesn’t work. Why is the user’s interpretation important? We can remember here 
Don Norman’s pioneering work, The Design of Everyday Things, where he talks 
about the gulf between the system image (the interface) and the user’s model (the 
perception of the interface formed by the user through interaction with it). If the user 
has a mental model of the interaction that doesn’t fit with the system image provided 
by the design team, then the user will be continually challenged by unexpected 
behavior from the system. An effective design language bridges the gap between the 
system image and the (assumed) user model.
As your language becomes richer and more complex, you need an efficient way to 
capture and share it. On today’s web, a pattern library is one of the key examples of 
good practice in supporting a design system.
7

### Sahifa 36

Pattern Libraries And Their Limitations
A design system consists not only of patterns, but also techniques and practices for 
creating, capturing, sharing and evolving those patterns. A pattern library is a tool to 
collect, store and share your design patterns, along with the principles and guidelines 
for how to use them. Even though pattern libraries have become popular on the web 
relatively recently, the concept of documenting and sharing design patterns in 
various forms has existed for a long time.
Palladio’s The Four Books of Architecture, first published in 1570 in Venice, is one 
of the most important and influential books on architecture. It is also one of the 
earliest examples of system documentation. Drawing inspiration from Greco-Roman 
architecture, Palladio provided rules and vocabulary for designing and constructing 
buildings, including principles and patterns, with detailed illustrations and 
explanations of how they work.

### Sahifa 37

Types of staircases: spiral, oval and straight. Palladio described how and when to use each type; 
for example, spiral staircases are suited for “very restricted locations because they take up less 
space than straight stairs but are more difficult to go up.”
In modern graphic design, systems have also long been documented, from early 
typography and grid systems, to Bauhaus design principles. For the last few decades, 
companies have documented their visual identities in the form of brand manuals, 
with NASA’s Graphics Standards Manual from 1975 being one of the more well-
known examples.

### Sahifa 38

Layout guidelines in NASA’s Graphics Standards Manual.
On the web, pattern libraries started as extended brand identity documents that 
focused on logo treatments, corporate values and brand styles, such as typography 
and color palettes. They then extended to include interface modules, as well as 
guidelines for their use. Yahoo’s pattern library was one of the first examples of 
documented interface patterns.
8

### Sahifa 39

Yahoo’s pattern library was one of the first examples of documented interface patterns.
For companies less resourceful than Yahoo, a pattern library would typically live in a 
PDF or a wiki, which meant that it was static and difficult to keep up to date. The 
aspiration for many designers and developers today is a more dynamic or “living” 
pattern library that contains the design patterns, as well as the live code used to build 
them. A living style guide or pattern library is more than a reference document — 
it’s the actual working patterns used to create an interface for a digital product.

### Sahifa 40

MailChimp’s pattern library is one of the most influential early examples of living pattern libraries 
on the web.
THE LIMITATIONS OF PATTERN LIBRARIES
Pattern libraries are sometimes thought of as interchangeable with design systems. 
But even the most comprehensive and living pattern library is not the system itself. 
It’s a tool that helps to make a design system more effective.
A pattern library doesn’t guarantee a more cohesive and consistent design. It might 
help to correct small inconsistencies or make a codebase more robust, but a tool 
alone will have very little impact on the user experience. No pattern library will fix 
bad design. Patterns can still be badly designed, misused or combined in ways that 
don’t work as a whole. As Michael McWatters, UX architect at TED, noted in an 
9

### Sahifa 41

interview: “Even a SquareSpace template can be ruined by sloppy design thinking.” 
And conversely, a product with a coherent user experience can be created without a 
comprehensive pattern library (as we will see in chapter 6 in the example with 
TED’s design system).
A living pattern library is associated with better collaboration. Yet you might end up 
in a situation where only a small group of people uses it, or there might be too many 
disconnected patterns as a result of a lack of communication between the teams. 
When up-to-date, a pattern library is a glossary for the shared language. But that 
doesn’t mean there isn’t still room for interpretation. It’s the discussions around the 
interpretation which are often the key to a pattern library’s success or failure.
On the other hand, pattern libraries are sometimes blamed for stifling creativity, 
leading to generic looking websites. But again, a pattern library reflects the design 
system behind it. If your system is fundamentally rigid and restricting, the pattern 
library can reveal and emphasize the rigidity. If it allows plenty of creative 
experimentation, a good pattern library can make the experimentation easier.
With all the automated tools and style guide generators available today, setting up a 
library of components can be done much quicker than in the past. But without a 
foundation of a coherent design system that integrates the patterns and practices, its 
impact will be limited. When a pattern library is used to support a solid design 
language foundation, it becomes a powerful design and collaboration tool. Until 
then, it’s a collection of modules on a web page.

### Sahifa 42

What Makes An Effective Design System
The effectiveness of a design system can be measured by how well its different parts 
work together to help achieve the purpose of the product. For example, the purpose 
of FutureLearn is “to inspire lifelong learning in everyone, anywhere.” We could 
ask, how effective is the design language of the interface to help us achieve this, and 
how effective are the practices of the team? If the interface is confusing and people 
don’t achieve their goals, then the design language is not effective. If it takes too 
long to build a new area of the site because patterns have to be recreated from 
scratch every time, then we know our practices can be improved. A design system 
can be considered effective when it combines cost-effectiveness in the design 
process, and efficiency and satisfaction of the user experience in relation to the 
product’s purpose.
SHARED PURPOSE
In Thinking in Systems, Donella Meadows explains that one of the most important 
qualities systems have is how they’re connected and organized: subsystems are 
aggregated into larger systems, which in turn form part of something larger. A cell in 
your liver is part of an organ, which is a part of you as an organism. No system exists 
in isolation. Your design system might have a smaller subsystem within it: editorial 
rules to control the layout of the page; or it might include a method for scaling your 
logo responsively in a certain way. At the same time, it is also part of other larger 
systems: your product, your team, your company culture.

### Sahifa 43

The Whitney Museum of American Art’s logo, a “dynamic W,” is a simple yet remarkably 
adaptable system in its own right. The W responds to the artworks and words around it, allowing a 
huge range of flexible layout possibilities.
In highly effective systems, we see that subsystems are connected and aligned 
toward a shared purpose: a design approach is mirrored in the front-end architecture; 
design patterns follow the guiding principles; the pattern language is applied 
consistently in design, code and the pattern library. We see harmony in the way those 
systems function: their workflow is more efficient, and the user experiences they 
generate feel more meaningful and coherent.
IDENTIFYING PROBLEMS
10

### Sahifa 44

When there are gaps, it’s also easy to see them. A fragmented design system leads to 
a fragmented user experience, full of conflicting messages. We want the user to sign 
up for our newsletter, but we also want them to check out our latest products. We 
want them to progress through the steps, but we also need to make sure they rate 
each recipe. “Sequence” is used to preview the steps in one area of the site; in 
another, it is suddenly a tabbed navigation. The interface is full of various shades of 
the same color and multiple versions of the same button. The team’s productivity is 
also affected: making the tiniest change is time-consuming and fiddly because of the 
confusing, tangled up code. Designers spend their time copying pixels and 
reinventing solutions to the same problems, instead of understanding and solving real 
user needs.
How do we reduce the gaps and make our design system more effective? By 
understanding what it is and how it works. We’ll start by looking at how a pattern 
language evolves in a new product, by taking a simple fictional ten-minute recipe 
website as an example.

### Sahifa 45

Example: A Ten-Minute Recipe Site
Imagine we are creating a website for sharing recipes with people who love healthy 
food but don’t want to spend a lot of time cooking. If we were to approach it with a 
system in mind and define design patterns early on, where would we start? Before 
we begin, let’s make some assumptions. We understand the domain of cooking, and 
enough research has already been done to inform our design decisions. So what 
we’re trying to do is not figure out what the experience should be, but see how we 
can establish design system thinking for this new website.
PURPOSE AND VALUES
One of the first things we’d do is try to understand who our users are, their goals, 
needs and motivations. To keep it simple, let’s say that we know they are busy 
professionals and their goal is to get a tasty, healthy meal without hassle and hours 
spent cooking. There are many ways we can help them achieve this goal: connect 
them with chefs, deliver food to their doorstep, build a conversational app. But we 
want to do it through a website with ten-minute recipes.
If we were to express the purpose in a single sentence, it would be along the lines of: 
Motivate and empower people to cook delicious healthy meals in no more than ten 
minutes. This purpose is the core of the product, and it should inform design and 
development decisions. The team should recognize that purpose and believe in it — 
it shouldn’t feel forced.
Another important element is the ethos that captures the values and spirit we try to 
portray through the site. For us it can be simple healthy food and experimentation 
with common ingredients. For other cooking sites it can be haute cuisine and mastery

### Sahifa 46

of culinary skills.
DESIGN PRINCIPLES
To make sure the purpose of the product is expressed clearly through everything we 
do, we would need to establish a few grounding principles and values. They might be 
discussed informally or written as a manifesto — what’s important is that the people 
involved in the creation of the product agree on those values and commit to them.
For example, everyone on the ten-minute cooking recipe site team understands the 
value of time. They are motivated by having a time limit on the recipes, and as a 
result they all strive to make interactions on the site short, simple, fast and smooth. 
This principle will be expressed not only through design patterns, but the 
performance of the site, its tone of voice, and even how the team operates.
These principles might not necessarily be official or even written down. But having 
an agreement and awareness in the team on what they are is essential to keep 
everyone’s effort and priorities in sync. It can also help with decision-making: from 
which feature to build first and which approach to use, to working out UX flows, or 
how buttons should look and the choice of typeface.
BEHAVIORS AND FUNCTIONAL PATTERNS
We’d work out some of the key behaviors we want to encourage or enable in our 
users that will help them achieve their goals.
We want people to always choose a healthy home-cooked meal over fast or 
microwaved food. This means that our meals need to look delicious and healthy,
and be more enticing than microwaved food. Good imagery with irresistibly 
delicious yet simple-looking food can help us here.
11
•

### Sahifa 47

We want to enable people to achieve good results in under ten minutes. This 
means that we’ll need to present the recipes in a few simple steps. The steps 
should be short, clear and focused. Perhaps we could have a timer on each step, 
to make sure we keep to the ten-minute promise.
We want to encourage people to be spontaneous and feel like they can prepare 
something whenever they like. Start with what you have already, rather than 
with what you need to get — no need to shop for extravagant ingredients. In 
terms of UI, this could be supported by easily selectable ingredient thumbnails 
with clear labels.
Finally, we want to encourage people to be creative and spontaneous, and to 
have fun. Show which ingredients are optional and what they can be replaced 
with. Show unexpected combinations that could be interesting to try.
Naturally, the design details will change as we work on the site, but those key 
behaviors would remain the same. Those behaviors will inform the core functional 
modules and interactions of the site: ingredient thumbnails, recipe cards, step 
sequence, timer.
AESTHETICS AND PERCEPTUAL PATTERNS
Around the same time, we’d need to work out how we want to be perceived by 
someone using the ten-minute cooking recipes site. Are we simple and down-to-earth 
or glamorous and sophisticated? Are we serious or playful? Bold or subdued? 
Utilitarian or emotional? What are the aesthetics that capture the personality and 
ethos we want to portray through the interface? We’d start thinking about the brand.
We’re passionate about healthy food, so we want it to come through the site. Perhaps 
it would have an organic, warm, wholesome feel. We also believe that cooking 
doesn’t need to take a lot of planning and preparation; it can be spontaneous and fun, 
and you can experiment and be creative in the ten-minute time limit.
•
•
•
12

### Sahifa 48

At this point we would probably put together some mood boards and start 
experimenting with visuals until the brand feels right. Once we achieve this, we 
can define core visual brand elements such as typography, color palette, tone of 
voice, and any distinguishing features of the brand; for example, illustrations, image 
styles, specific shapes, unique interactions that capture the essence of our service and 
present content in the best way.
Let’s say we come up with a warm, earthy color palette, hand-drawn icons, 
typography with a focus on readability, quality photography of healthy food, and a 
few simple interface elements and controls. These styles will become our perceptual 
patterns.
SHARED LANGUAGE
Alongside this process we will be making language decisions by choosing to refer to 
concepts in certain ways. What is a “recipe”? What do we mean by “steps”? What 
makes a “delightfully simple” interaction? The words we choose will influence how 
the team thinks. And indirectly, they will shape the design.
At first, the patterns and language choices will be shared informally. But as our team 
and the product grow, so will the language. Eventually we’ll need a more structured 
way to capture, share, and organize our design vocabularies.
Now that we’ve looked at the design process in a nutshell using a fictional site, we 
can look at how systems evolve, using examples from real-world digital products 
and companies.
—
1.
The patterns on FutureLearn are chosen to support reflective learning. The learner needs to 
focus on the task at hand and not be distracted by displacement activities. The goal was to 
create an atmosphere that feels calm and contemplative.
13
14

### Sahifa 49

2.
The website UI Patterns is a great source of common design patterns, grouped by purpose 
and the design problem it solves. For a comprehensive read on UI patterns, I also 
recommend Designing Interfaces: Patterns for Effective Interaction Design by Jenifer 
Tidwell.
3.
http://smashed.by/patternsrecognition
4.
Until the swipe gesture had emerged as a mobile pattern, no one would have known how to 
engage with it. Now we see whole products built on this pattern (such as Tinder). The 
transition to using what people know and exploring something new is very delicate; products 
live and die based on when and how they do this.
5.
http://smashed.by/researchingsystems
6.
http://smashed.by/visualloudness
7.
The challenge is also not to impose one definition or conception of “Sequence,” but to 
understand and work with its context of use so that, for example, the UX team can support 
different types of sequencing (for FutureLearn, sequencing of courses, runs, steps, user 
actions, etc.) within a coherent framework.
8.
Perhaps this is how we can distinguish style guides from pattern libraries. Style guides 
traditionally focused on styles, such as colour and typography. Pattern libraries can include 
styles, as well as functional patterns and design principles, among other things.
9.
http://smashed.by/mailchimppatterns
10. http://smashed.by/whitneyidentity
11. In the next chapter we will look in more detail at the qualities of effective design principles 
and how they can form a foundation of your design language.
12. For further reading on understanding what people want, and shaping a vision for a new 
product, see “We Don’t Sell Saddles Here” by Stewart Butterfield, CEO of Slack.
13. More about the process of defining perceptual patterns in chapter 4.
14. In chapter 5, we will see how effective names and a collaborative naming process can 
become part of the foundation of a design language system. In chapter 10 we will look at 
pattern libraries as a way to capture language choices and establish a shared vocabulary.

### Sahifa 50

CHAPTER 2
Design Principles
Solid principles are the foundation for any well-functioning system. In this chapter 
we’ll discuss the qualities of effective design principles and look at some of the ways 
of defining them.
Earlier we talked about the importance of starting with the purpose and ethos of the 
product when designing the interface. Having clarity on the purpose is paramount 
because all other decisions should be shaped by it, even if indirectly. How do we 
make sure that the purpose of the product is manifested through design? By 
establishing a few grounding values and principles.
In some companies, especially early on, trying to articulate shared guidelines can be 
hard. Design principles are not something that can be measured and quantified, and 
defining them can take a few iterations. There might also be some confusion about 
what principles are exactly. Depending on the company, they can be more focused 
on the brand, the team culture, or the design process. The principles at Pinterest are 
more brand-focused (“Lucid,” “Animated,” “Unbreakable”), whereas at the UK’s 
Government Digital Service (GDS) they’re directed more at how the team operates 
(“Do less,” “Iterate. Then iterate again”).
Sometimes principles are used for a limited time, for a specific project. Designer 
Dan Mall likes to write a “design manifesto” at the start of every project, to make 
sure creative direction and objectives are clearly expressed. In other cases, 
principles are more long-lasting, and their heritage becomes part of the company 
ethos. Take Jack Daniel’s values of “confidence,” “independence” and “honesty,” 
which have remained the same for the last century.
Larger companies might have separate sets of principles for the user experience, the 
brand and the design system. Additionally, each team working in a company might 
also have their own team principles. While this works for some, others can find that 
1
2
3
4
5

### Sahifa 51

having multiple sets of guidelines can contribute to a design system’s fragmentation. 
At Atlassian, an enterprise software company, the principles for marketing and for 
the product were initially different. Over time, the team brought them closer 
together, and they are now working on a unified set of principles, with the goal of 
having a shared philosophy to bridge the gap between the disciplines of marketing, 
product and support.
“It is one system. The principles are there to connect the dots.”
— Jürgen Spangl, head of design, Atlassian
Instead of having a separate set of principles for different teams and parts of the 
system, Atlassian aims to have a few key values — such as “Bold,” “Optimistic” and 
“Practical, with a wink” — going across all the touchpoints in the customer journey 
of Atlassian products. While those values are the same throughout the journey, they 
are not represented with the same level of intensity at different stages. There is a lot 
of “boldness” in the sales and marketing areas of the site, to showcase the products 
and help people understand their value. But once you get to the product itself and 
support areas, the experience becomes more about getting the work done and making 
sure people are able to be as effective as possible. So the boldness is toned down and 
the “practical” value is shifted up. As Kevin Coffey, design manager at Atlassian 
noted: “Nobody wants a bold support page.”

### Sahifa 52

Qualities Of Effective Design Principles
Approaches to design principles are unique to every company and can take many 
forms. Principles can be overarching or more granular, temporary or long-lasting. 
What matters is how effective they are at unifying design thinking and distributing 
creative direction in the team. In the context of this book, design principles are 
shared guidelines that capture the essence of what good design means for the team, 
and advice on how to achieve it; in other words, agreed criteria for what constitutes 
good design in your organization and for your product.
Regardless of your approach, effective guidelines typically have these qualities in 
common.
1. THEY’RE AUTHENTIC AND GENUINE
I’m sure you’re familiar with these principles: “Simple. Useful. Enjoyable.” They are 
ubiquitous, we hear them everywhere. There’s no argument that products that are 
designed well follow a certain set of common principles (take Dieter Rams’ ten 
commandments of good design, for example). But qualities like these should be a 
given — they should be done by design — along with other concerns, such as 
accessibility and performance. I’ve yet to see a consumer digital product which has 
“Complex,” “Useless,” and “Painful to work with” among its principles.
Knowing that your product should be useful and enjoyable is not going to be hugely 
helpful in guiding your design decisions, because these qualities can be interpreted in 
a variety of ways. What would make them more helpful is knowing exactly what 
those words mean to your team and your product. What does innovative entail? 
When is a design considered useful? How do you know if it’s really delightful? Good

### Sahifa 53

design principles define qualities that can be interpreted in different ways, and 
ground them in the context of a specific product.
Let’s take TED as an example. One of TED’s design principles is “Be timeless, not 
cutting edge.” The word timeless is specific not only to TED’s interface but its entire 
brand and design approach. And this means they are not going to adopt a new 
technology or introduce a design element for the sake of following a trend. First and 
foremost, it has to serve a purpose, and it has to work for as many users as possible. 
For TED, timeless means not only simplicity but also being conscious of stylistic 
features that have no proven benefits to users. The team wouldn’t introduce a 
parallax effect, for example, even though it feels very current, unless it solved a real 
design problem.
2. THEY’RE PRACTICAL AND ACTIONABLE
A principle should offer practical guidance on how to solve a design problem within 
the context of a specific product. Compare these two versions of one of 
FutureLearn’s principles:
“Make it simple. Make it so simple it’s almost invisible! We should 
always work to remove friction on the platform, creating an experience 
that allows users real freedom to the content. If our platform is easy to 
understand, people can and will use it more.”
This statement makes perfect sense — no one can argue with the need to have a 
simple and usable interface. However, it’s not clear from this advice exactly what 
simplicity means and how to achieve it. Compare it with this version:

### Sahifa 54

“No needless parts. Every design element, from the largest to the 
smallest, must have a purpose, and contribute to the purpose of a 
larger element it is part of. If you can’t explain what an element is for, 
most likely it shouldn’t be there.”
In practice, the question “Is it simple?” is much harder to answer objectively than 
“Does this contain needless parts?” The latter can be acted on by going through the 
interface and questioning the purpose of every element.
To phrase the principles in a more practical way, try thinking of them not as 
something that should merely sound good, but something that offers actionable 
advice. Imagine a new person joined your team and you’ve been asked to share five 
things that are most important when designing for your product. If you tell them “We 
like things to be delightful here. Make it delightful!” it’s probably not going to help 
them do their job. You’d need to define what delight means and share practical 
examples of what delight looks like in the context of your interface.
Let’s take a look at a couple of examples of design principles and how they can be 
made more practical.
Vague: “Make it clear.”
Practical: “Only one number 1 priority. What do you want your users to see and do 
first?”
Vague: “Make it simple.”
Practical: “Make it unbreakable. Just like a children’s toy, make sure it is designed 
for exploration and impossible to mis-tap.”
Vague: “Make it useful.”
6

### Sahifa 55

Practical: “Start with needs. If you don’t know what the user needs are, you won’t 
build the right thing. Do research, analyze data, talk to users. Don’t make 
assumptions.”
But even the best-worded principle can still be interpreted in a variety of different 
ways. Nothing can make a principle more practical than pairing it with a real-life 
example to show how it can be applied in practice. Find specific parts of your 
interface where a principle is clearly represented and connect the two together. Can 
you point to a place which clearly shows having “only one number 1 priority”? Can 
you demonstrate how a pattern can be truly “unbreakable” despite having rich 
interactions?
3. THEY HAVE A POINT OF VIEW
Design is shaped by the choices we make. Should this page be more visually alive or 
more utilitarian? Is it appropriate to be more playful or more serious here? Can we 
justify making this module more usable at the cost of making it less flexible? By 
achieving some things we often have to say no to others. Good design principles help 
to work out priority and balance, even if there are conflicting factors to consider.
Take the Salesforce Lighting Design System principles as an example: “Clarity. 
Efficiency. Consistency. Beauty.” It’s emphasized that they must be applied in the 
priority order above. Beauty should not be promoted over efficiency or consistency, 
and clarity should always come first. Ranking the principles in this way 
communicates to the team what should take priority when making design decisions.
It can be useful to acknowledge the conflicting values and suggest how to find a 
balance. One of the early design principles at Medium was “Direction over Choice.” 
This principle was often referred to while the team was designing the Medium editor. 
They purposely traded a variety of formatting options for guidance and direction to 
allow people to focus on writing.
7
8
9
10

### Sahifa 56

The few options available in Medium’s minimal editor clearly illustrated one of Medium’s 
principles, “Direction over Choice.”
Good principles don’t try to be everything for everyone. They have a voice and 
actively encourage a designer to take a perspective. This idea has been emphasized 
by Dan Mall in “Researching Design Systems ”:
“A design system should have guidelines for: perspective, point of 
view, extending creative direction to everyone that decides to build 
something with the design system. That stuff should be baked in. 
Otherwise, we all might as well use Material Design and call it a day.”
— Dan Mall
4. THEY’RE RELATABLE AND MEMORABLE
Here’s a fun test. Try asking people in your company what your design principles 
are. If no one can remember them, chances are they can be improved. To be 
memorable, the principles must be in constant use. They should be referred to in 
11

### Sahifa 57

everyday conversations, included in presentations and design critiques, displayed 
where they can be seen. And to be in use, they must be genuinely useful, possessing 
the qualities above.
It also helps not to have too many of them. Human memory is limited and 
remembering more than four things at a time can be hard. The optimal number of 
design principles — if you want them to be in use — is between three and five. 
When the teams at TED, Atlassian and Airbnb were asked about their design 
principles during interviews for this book, they were all able to recall them instantly. 
There wasn’t a moment’s hesitation; no one got confused or tried to look up the 
principles in a brand manual. How could they remember them so well? Their 
principles were simple, relatable, useful — and there weren’t many of them.
Most importantly, the teams used them on a daily basis for making design decisions. 
Airbnb’s four design principles (“Unified,” “Universal,” “Iconic,” “Conversational”) 
are deeply engrained in its design process:
“When we design a new component, we want to make sure it addresses 
all four of those. If we didn’t have a set of principles it would be 
difficult to agree on things. We want to make sure each piece lives up 
to it.”
— Roy Stanfield, principal interaction designer, Airbnb
The team at Spotify came up with the acronym TUNE (tone, usable, necessary, 
emotive) to make their design principles more memorable. Asking if a design is “in 
TUNE” during critiques and QA sessions has become part of Spotify’s design 
process.
12
13

### Sahifa 58

Making sure your principles possess the qualities above takes time, commitment and 
teamwork. But it’s worth the effort — a core set of principles are at the heart of any 
design system.

### Sahifa 59

Defining Your Principles
Expressing your design approach in five sentences is not easy. Every team arrives at 
their principles in their own way: some go through rounds of workshops, others 
might get input from their CEO or a creative director. Regardless of how you get 
there, the following tips can be useful to keep in mind.
START WITH THE PURPOSE
Design principles must support the larger purpose of the product and help express 
the product’s ethos. If you aren’t sure where to start, look first at your company’s 
overarching values or a product vision, and then try to work out how design 
principles can contribute to that larger goal.
The main purpose of TED’s website can be captured in one sentence: “Spread the 
ideas as far and as wide as possible.” In terms of TED’s ethos and values, this means 
reaching as many people as they can, lowering the barrier to entry, and making the 
product inclusive and accessible. It means prioritizing performance and accessibility 
over flashy features, clarity of message over bold experimental design. Their 
“timelessness” principle encompasses that.
FIND SHARED THEMES
If you’re still in the process of defining your principles, a useful exercise is to ask a 
few team members (or everyone, depending on size of the team) to write them down 
individually. What, in their opinion, does good design mean for your product? How 
would they explain it in five sentences to a new member of the team, in a way that’s 
practical and easy to grasp?

### Sahifa 60

Ask them to find a practical example in your product’s interface and include it 
alongside each principle.
Comparing your team’s answers can reveal how much unity you have in your design 
approach. Are there many shared themes and overlaps? Have different disciplines 
ended up with similar principles? It’s always interesting to see everyone’s responses, 
in particular how they differ between people who have just joined the team, and 
those who’ve worked on the product for some time. These answers can be a valuable 
starting point in further work on the principles, as you identify common themes and 
agree on priorities.
FOCUS ON THE RIGHT AUDIENCE
A surefire way to end up with vague design principles is to have no idea who they’re 
for. Are you writing for a corporate identity brochure? For the company website? A 
careers website? Potential partners and customers? Try writing your principles for 
yourself and for your colleagues, first and foremost: designers, developers, content 
producers, marketing professionals, domain experts — people directly involved in 
the creation of the product. Aim to come up with an informal agreement on what 
constitutes good design for your product, and offer practical guidelines for achieving 
it.
TEST AND EVOLVE YOUR PRINCIPLES
As your product evolves, so will your principles. They will be shaping the design 
language, which in turn will be shaping the principles. Or they might start off being 
clear and focused, but over time become more diluted and lose their authenticity. To 
make sure your design principles continue to improve, they need to be constantly 
tested, evaluated and refined. This can only be done by being conscious of them and 
applying them in your work every day. By making your principles part of design

### Sahifa 61

critiques, for example, you can continuously test if they help in your design process, 
and if not, continue iterating them.

### Sahifa 62

From Principles To Patterns
One of the challenges I’ve had in my work as a designer is working out how to 
materialize higher-level concepts, such as design principles and brand values, into 
concrete UI elements. How exactly are they embodied in the design patterns we 
create?
A lot of it is about choice and execution of patterns. For Medium, on the functional 
level a rich-text editor was required. It could have been any kind of editor, with any 
degree of complexity. But out of all the possibilities, Medium chose the simplest 
one, guided by its principal, “Direction over Choice.”
For TED, clarity of message is valued over aesthetics. Trying to distill a talk into a 
single sentence can be hard, and sometimes titles can be long. It would be easier to 
clip the title, but for the team the message of the talk must always take priority. 
Instead of opting for an easier solution, they make sure that their design patterns can 
accommodate long titles.
The hero banner pattern on a TED.com talk screen can accommodate long titles, which is in line 
with their design principles.
There’s a sense of prioritization also from the brand standpoint. For example, The

### Sahifa 63

TED team chose not to introduce a new image-rich home page until they developed a 
compression tool to minimize the impact such imagery would have on performance.
For the team at Atlassian, the “optimistic” principle is embodied in an “optimistic 
interface. ” In JIRA, for example, when a user has to move a card from “In 
progress” to “Done,” cards are allowed to be moved right away, providing an instant 
response to the user, even though in the background there are a lot of checks and 
validations, and many things that can go wrong. They aim to express the “practical 
with a wink” principle through the friendly language of the copy, feedback 
messages, on-boarding, and other places throughout the site.
Design patterns are shaped by the core idea of how a product works. Think about 
how an ethos of “transparency and collaboration” is embodied through open 
channels on Slack; how the idea of “capturing life’s unique moments” translates into 
Instagram’s photo feed and interactions; or how cards on Trello (a functionality that 
goes back to the seminal HyperCard system) encourage a certain type of workflow.
The choice and execution of the patterns and their unique combination are influenced 
by a product’s purpose, ethos and design principles. You can view design principles 
as grammar rules for creating patterns and combining them in ways that make 
intrinsic sense. Equally, as the brand and functional patterns evolve and become 
more refined, they shape the design principles. Principles and patterns are refined 
and influenced by one another continuously.
Over the next two chapters we’ll talk about design patterns in more detail, taking 
real-life products as examples. We’ll see how design patterns emerge and how they 
are affected by a product’s purpose and ethos, user behaviors, brand, business 
requirements, and other factors.
—
1.
http://smashed.by/pinterestredesign
14

### Sahifa 64

2.
http://smashed.by/govukprinciples
3.
“So…What Do I Make?” by Dan Mall
4.
“When It Comes To Whiskey, America Knows Jack” by Avi Dan
5.
Google has well known broad-brush design principles such as “Focus on the user and all else 
will follow,” and a more specific set of principles for its material design language, such as 
“Motion provides meaning.”
6.
Example adapted from Pinterest design principles in “Redesigning Pinterest, block by 
block”.
7.
Example adapted from GDS design principle.
8.
This point was inspired by the excellent article “A Matter of Principle” by Julie Zhuo.
9.
http://smashed.by/lightning
10. “Creating useful design principles” by Dustin Senos
11. http://smashed.by/researchingsystems
12. For further reading on the limitations of human working memory see “The Magical Mystery 
Four: How is Working Memory Capacity Limited, and Why?” by Nelson Cowan.
13. “Design Doesn’t Scale” by Stanley Wood
14. http://smashed.by/truelies

### Sahifa 65

CHAPTER 3
Functional Patterns
In this chapter we’ll discuss the role of functional patterns and why they should be 
defined early in the design process.
Functional patterns are the tangible building blocks of the interface. Their purpose is 
to enable or encourage certain user behaviors.
On the ten-minute cooking site, some of those behaviors included selecting 
ingredients, choosing a recipe, and following steps within an allocated time. The 
functional patterns we design will be informed by those behaviors. Functional 
patterns, or modules , are largely shaped by the domain a product belongs to. The 
patterns in our cooking app would be quite different from, say, finance software. 
Instead of recipe cards we’d be dealing with task bars, data fields, grids, charts and 
graphs.
Functional patterns can be simple or they can combine to create more complex 
patterns. A recipe card is made of a meal title, image, ingredients, and an action 
button. Each module within the recipe card has its own goal: the title tells us what 
the meal is; the image provides a preview of the final result; ingredient icons allow 
us to scan the cards more easily. Together, those modules help to achieve a shared 
purpose: to encourage people to cook the meal shown on the recipe.
As the product evolves, so do the patterns. We might start allowing our users to rate 
the recipes, and the rating display will become part of the recipe card. Or we might 
decide that the layout of the card can be improved, or that ingredient icons should be 
made clearer, or that we need to introduce a compact version of the card. We test and 
iterate the patterns to try to make them work better to achieve their purpose; that is, 
encouraging the behaviors more effectively.
Articulating the purpose of the patterns early in the design process can help prevent 
1

### Sahifa 66

duplication as the product grows. At first, it might not seem to be worth the effort; 
after all, a product can change too fast in its early days to be able to pin down all the 
interface parts. But do the core functional patterns really change that much? Let’s 
take FutureLearn as an example and see how the interface evolved in the three years 
since the initial design.

### Sahifa 67

Patterns Evolve, Behaviors Remain
Since it was founded by the Open University in 2013, FutureLearn’s vision has been 
to “inspire all to learn through telling stories, provoking conversation, and 
celebrating progress.” To be able to do that, as a minimum we had to make sure 
people could discover and join an online course, motivate them to progress through, 
and make the learning experience rewarding and stimulating. This vision informed 
the initial functional patterns on FutureLearn.
Courses are arranged in units and there’s a linear flow to them — one part leads to 
another. On the interface level, this translates into a weekly structure. Each week is 
broken down into activities, and activities into steps. The course progress module is 
one of the core functional patterns: it allows learners to navigate the content of the 
course, shows their progress, and where the course is currently active.
Course progress module on FutureLearn.
These patterns went through a few changes after they were first designed over three 
years ago. Their styles, and even functionality and interactions, have changed. Yet 
their purpose fundamentally stayed the same, as it’s connected to the core idea of 
how FutureLearn works.

### Sahifa 68

The To Do page went through several revisions over the course of three years but the purpose of the 
core modules stayed the same.
Similarly, discussion threads on FutureLearn have evolved over time, as the volume 
of people participating has increased: the layout of the threads, the interactions and 
the filtering features have evolved, but their core purpose remains largely the same 
— to engage learners in conversation and allow them to learn from each other.
Discussion pages went through several iterations once they were designed but the purpose of the 
core modules was unchanged.
The core unit for displaying course details has also evolved over three years, to allow 
users to see a larger selection of course listings before needing to scroll down the 
page. But again, the purpose of the pattern remains the same — to allow people to 
discover and join the courses they’re interested in.

### Sahifa 69

Course list evolved over years, to allow users to see a larger selection of course listings.
As often happens in the early start-up days, because of time constraints and other 
priorities, many core functional patterns weren’t defined. As FutureLearn’s interface 
and educational functionality grew, patterns were duplicated. We ended up with 
several course progress modules, variations of a comment module, and a few 
different course blocks and course cards across the site. Perhaps this was inevitable. 
Or could some of those duplications have been prevented?
When a pattern is not defined and shared in the team, you start recreating it to 
accomplish similar goals: another promotional module, another news feed, another 
set of sharing links, another dropdown. Before you know it, you end up with 30 
different product displays and pop-over menus.
Patterns are the physical embodiment of the behaviors we’re trying to encourage or 
enable through the interface. Their execution, content, interactions and presentation 
can change. (In fact, patterns don’t even have to be visual — they can be read out by 
a voice, or embodied in another way.) But the core behaviors they’re designed to 
encourage remain relatively stable, as they stem from the purpose of your product 
and the idea of how it works. Being conscious of the purpose of your key patterns 
can help you understand how your system works and prevent it from fragmenting as 
it evolves.

### Sahifa 70

Defining Functional Patterns
Defining patterns early in the design process doesn’t have to take a lot of time. There 
are techniques that can be integrated into your process without extra effort. Here are 
a few that I find particularly helpful.
CREATE A PATTERN MAP
To map out your customers’ needs, goals and motivations you might have done 
customer experience mapping , “job to be done,” or a similar exercise around 
customer journeys. The outcomes typically feed into the early design explorations 
and prototypes. At this point, there’s usually a fairly clear understanding of the 
behaviors we want to encourage or enable in our users: learn about a course, join a 
course, engage in a discussion. But once we focus on the interface, sometimes we get 
lost in the details. We spend time making the most impressive page header, 
forgetting what this header is for and how it affects the user in different parts of their 
journey. In other words, we lose the connection between user behaviors and the 
exact patterns that encourage or enable those behaviors.
To see how your patterns fit into a bigger picture, try to map some of your core 
modules to the sections of a user journey. Think about what each section is for and 
what behaviors it’s designed to encourage. You don’t need to worry about capturing 
every icon or button at this point. Focus on the big picture: understand the parts of 
the system and how they work together. For FutureLearn, it was primarily focused 
on three areas: discovering content, learning on a course, and achieving a goal.
2
3

### Sahifa 71

Some of FutureLearn’s functional patterns mapped to three key stages of a user journey.
Keeping this map in my mind helped me to think in families of patterns joined by a 
shared purpose, rather than individual pages. For example, instead of designing a 
course list page, I’d think of the “Discovery” area as a whole. What are the behaviors 
we need to encourage at this stage of the user journey? What are the patterns that can 
support those behaviors? Where else on the site do they exist and how do they work 
there? If it’s a new pattern, how does it contribute to the whole system? Thinking of 
all these questions is part of designing systematically.
CONDUCT AN INTERFACE INVENTORY
The interface inventory process , described by Brad Frost, has become a popular way 
to start modularizing an interface. The idea is simple. You print out the screens of 
your interface on paper, or collect them in Keynote or PowerPoint. You then 
separate out various components either by cutting them out or pasting them in 
Keynote.
4

### Sahifa 72

An interface inventory showing some of the interactive elements.
You end up with a collection of parts which can be grouped into categories: 
navigation, forms, tabs, buttons, lists, and so on. Going through this process allows 
you to see duplicated patterns, and identify problem areas that need attention. This is 
when you discover that you have dozens of headers or pop-over menus, and start 
thinking about how to bring some order to all that.
An inventory doesn’t have to encompass everything (although the very first one you 
do should be comprehensive). It can focus on one pattern group at a time, such as 
promotional modules, headers, or all the product display modules. You can do an 
inventory focused specifically on typography, or color, or animations.
To be most effective, interface inventories should be done regularly. Even if your 
team maintains a pattern library, new patterns will emerge that need to be folded into 
the system. If you get into a habit of running inventories every few months, each 
time shouldn’t take more than a couple of hours. And every time you do it, you 
understand your system better and can improve it.
VIEW PATTERNS AS ACTIONS
5

### Sahifa 73

To understand the purpose of a pattern, try focusing on what it does rather than what 
you think it is. In other words, try to find an action that best describes the behavior a 
pattern is designed for. Describing a pattern with a verb rather than a noun can help 
you to broaden potential use cases for a pattern and define its purpose more 
accurately.
Say you’ve introduced a simple module to promote an online course. If you try to 
describe what it is, you might refer to it as “Image header” or “Course banner.”
UI component promoting an online course on FutureLearn.
But by describing a pattern in this way, you could be making it too specific to its 
presentation or content. You might end up limiting its use to a particular context. On 
the other hand, if you define it in terms of actions — from your user’s perspective as 
well as your own — you can uncover its purpose: “Promote a course” and “Discover 
a course”; and “Get inspired to join a course” and “Encourage people to join.” By 
focusing on the action, you connect pattern with behavior and keep it open for 
various use cases. What else can this pattern promote? An online discussion? A new 
event? The name you give it should also reflect this. In the example above, we 
named the module “Billboard” to reflect its action-focused, promotional function.
DRAW A PATTERN’S STRUCTURE
To get a shared understanding of how a pattern works, draw its structure: the core 
types of content a module needs to be effective.

### Sahifa 74

Designers, developers and content strategists can do it together when working on a 
new module, or when refactoring an existing one. Start by listing the core content 
elements a module needs to be effective. For example, you might agree that in your 
interface a promotional module like “Billboard” needs:
a heading
a strong call to action
an eye-catching background (solid color or image)
Next, try to determine the hierarchy of elements and decide how they should be 
grouped; for example: is the image part of the content? Is a label always necessary? 
While doing that, make a few sketches to visualize the structure. To give you an idea 
of what it might look like, here’s an example of the content structure for a course list 
item module on FutureLearn.
Example of the content structure for a course list item on FutureLearn.
At this point you might be thinking: “It’s just a sketch or a wireframe. I do that all 
the time anyway.” But it’s a bit different. This is a sketch focused specifically on the 
content structure of a module, and the hierarchy and grouping of the elements.
•
•
•

### Sahifa 75

Once you have a shared understanding of a pattern’s structure, it’s easier to make 
sure that the way the module is designed is reflected in the markup. A designer can 
work on the visual explorations, while a developer can start putting together a 
prototype (or both can prototype, depending on how you work). Designers 
understand how much they can push a pattern visually before it becomes something 
different. Developers know the reasons for the design choices and don’t get 
unexpected designs thrown to them over the wall. Everyone is aware of how the 
pattern is constructed and how changing it will affect other places.
Here’s another example. On FutureLearn we used to have four different versions of a 
social feed in different areas of the site — two versions of “Comment,” a “Reply” 
and a “Notification.”
Four different versions of social feed modules on FutureLearn.
While at first glance they looked similar, they didn’t share the same styles; that is, if 
you changed one of them, the changes wouldn’t apply to others, there were visual 
inconsistencies in spacing and typography, and so on.
Breaking them down and drawing their structures allowed us to see if they could be 
unified into one pattern, and to design that pattern in a way that works in all four use 
cases.
6

### Sahifa 76

The content structure for a “Feed item” module on FutureLearn.
Content structure is closely linked to the purpose of a pattern, as these examples 
have shown. Knowing how a module is structured helps us understand how it works.
PLACE PATTERNS ON A SCALE
Try placing similar patterns on a scale, in relation to one another. For example, there 
could be a few promotional patterns in your system, with varying degrees of 
intensity. Similar to the visual loudness scale I mentioned in chapter 1, promotional 
modules can be compared with one another.
Promotional modules can be placed on an imaginary visual loudness scale.
Placing patterns on a scale can help make sure they’re used appropriately and don’t 
compete for attention across the system. It also helps prevent modules being 
7

### Sahifa 77

recreated needlessly, since you can see when you already have a module at the same 
“volume.”
Another way to think about it is to imagine that your interface is not visual, but that 
it’s being read out by a voice. When would that voice need to get louder and change 
intonation? Think about how that volume and intonation can be expressed visually, 
through the relationships between the elements within the modules, as well as their 
hierarchy in the overall design. Thinking of it this way, of course, also has an 
additional advantage of making it more accessible to screen readers.
TREAT CONTENT AS A HYPOTHESIS
Here’s a paradox. We’re expected to design content-first, but at the same time we’re 
expected to build modules in a way that can fit any kind of content. A way to do this 
is not necessarily by starting with content, but with the purpose. Then we can treat 
content not as a known asset but as a hypothesis. This allows us to test if we’ve 
defined the purpose of the module well, and if the design works for that purpose.
Suppose we have a module, which was designed for displaying product features.
An example of a module designed for presenting product features.
We could define its purpose as “Supporting the main message with additional bits of 
easily scannable information.” The “bits” could be key features, short pieces of 
advice, or quick steps. We can build a pattern for content that fits this hypothesis 
(concise and scannable, supplementary rather than the main content on the page),

### Sahifa 78

and then test it.
If content consistently ends up being unsuitable for this pattern, it’s typically caused 
by one (or more) of these three reasons:
We didn’t correctly define the purpose of the pattern. Go back to trying to 
understand the behaviors it’s been designed for.
We didn’t design the pattern in a way that achieves its purpose best. Try a 
different design for this pattern.
We’re trying to force the content into a pattern that’s not quite right for it. 
Consider revising the content, or try another pattern.
When we don’t start with the purpose and the structure, we can end up with modules 
that are too closely tied to their content. For example, we had a case at FutureLearn 
where the copy was pushing important tabs below the visible area.
An example of a fragile module, which was too specific to its content.
The tabs were meant to stay visible. To get around the problem, we almost 
introduced a custom smaller size heading, simply to nudge the tabs up a bit. But had 
we done that, we would have ended up with a module that wasn’t robust. If the title 
•
•
•

### Sahifa 79

got longer or if we added an extra line, we would have been stuck with the same 
problem. Had we started with the purpose of the module and its structure, the tabs 
would probably have been placed at the top, since they’re such an important element 
of design.
These are just some of the tools and techniques you can try to define functional 
patterns in your interface. The most important thing is to understand how patterns 
link to the behaviors they were originally designed for: their purpose.
The purpose determines everything else that follows: the structure of the pattern, its 
content, its presentation. Knowing the purpose of the pattern (knowing which 
behaviors it’s designed to encourage or enable) can help us design and build more 
robust modules. It can help us know how much a pattern can be modified before it 
becomes something entirely different. And it can reduce duplication by giving the 
whole team a common point of reference, and connecting them with the original 
design intent. Being clear on the purpose also makes it easier to test the patterns to 
see how effective they really are.
If functional patterns are objects in the interface, then perceptual patterns are more 
like styles — they describe what kind of objects they are and how they feel. Let’s 
take a closer look at them.
—
1.
If we had to make a distinction between the two, I see functional patterns in a more generic 
way, as a kind of a Platonic ideal, and modules as the embodiment of functional patterns, 
which can be different in different interfaces.
2.
http://smashed.by/mappingxp
3.
“Job to be done” (JTBD) is an exercise that helps you focus on the underlying motivation 
behind using a product or service, rather on the product itself. For example, even though 
customers say that they buy a lawnmower to “cut grass”, their higher purpose might be to 
“keep the grass low and beautiful at all times,” which might indicate that a lawnmower is not 
the right tool for the job in the first place.

### Sahifa 80

4.
http://smashed.by/uiinventory
5.
In chapters 7 and 8 we will look at the interface inventory process in depth, starting from the 
purpose of the system and going down to the smallest patterns, such as icons and colors.
6.
In chapter 8 we’ll discuss in more detail when to unify patterns, when to split them up, and 
when to create variants.
7.
http://smashed.by/visualloudness

### Sahifa 81

CHAPTER 4
Perceptual Patterns
In this chapter we’ll discuss how perceptual patterns work and their role in a design 
system.
Imagine we both have a house, with the same set of furniture: a table, a few chairs, a 
bed, and a wardrobe. Even though the furniture is the same, our houses can feel 
distinctly different: it could be because of the style of the furniture, the materials, 
colors, textures, the fabric on the bed covers, the style of the ornaments, how we lay 
out the room, the lighting, or even the music we play inside. I refer to such attributes 
as perceptual patterns. Because of them, your house might feel like a bohemian lair, 
and mine like a warehouse.
Examples of perceptual patterns in digital products include tone of voice, 
typography, color palette, layouts, illustrations and iconography styles, shapes and 
textures, spacing, imagery, interactions or animations, and all the specific ways in 
which those elements are combined and used in an interface. Perceptual patterns are 
always present, even if they’re not purposefully designed. Even a purely functional 
tool has an aesthetic.
Sometimes such qualities are seen as styling or the skin of a product — a layer on 
top. But to be effective they must live not only on the surface but at the core of the 
brand, and they should evolve with the product. When effective, perceptual patterns 
become powerful product differentiators.
PERCEPTUAL PATTERNS HELP TO EXPRESS BRAND 
IMAGE
Products can feel different, even if they belong to the same domain and have similar 
modules. To write this book I tried dozens of word processors with very similar 
1

### Sahifa 82

functionality. Only a couple of them, including the one I’m using now, had the kind 
of writing environment that helped me focus and be most productive. I can describe 
it as crisp and calm, exhibiting a distraction-free aesthetic with an accent on 
important things, such as the display of the document outline, or the small circles 
which turn green as I approach my “writing goal.” This environment is created 
through a combination of certain patterns, although at a first glance it’s not easy to 
pinpoint what they are.
Let’s take another example: Spotify. To me it feels warm and personal. What exactly 
are the patterns that create the ambience of intimacy in this digital music service 
interface with over 100 million monthly users? As well as the functionality, it’s 
largely due to the imagery styles, color combinations (particularly the ratio of green 
to black), the subtle and calm feel of interactions, and the typography choices.
The ambience of intimacy on Spotify is the result of a combination of perceptual patterns, such as 
subtle interactions, subdued imagery and color accents.
On the other hand, the playful, creative, openly enthusiastic and slightly offbeat 
character of Smashing Magazine is conveyed through a different set of patterns — 
from the bold color palette and illustrations, down to the smallest details, such as a 
2
3

### Sahifa 83

slight angle on some of the interface elements.
The character of Smashing Magazine is conveyed through a variety of perceptual patterns — from 
typographic treatments to the playful angle of the images and icons.
Perceptual patterns express the brand through the interface and help to make it 
memorable. Take a look at the images below: can you recognize which products they 
represent?


> **Eslatma**: 83/284 sahifadan so'ng hajm chegarasiga yetdi.