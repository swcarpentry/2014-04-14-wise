---
layout: lesson
root: ../..
title: Introducing the Shell
level: novice
---
<div class="objectives" markdown="1">

#### Objectives
*   Explain how the shell relates to the keyboard, the screen, the operating system, and users' programs.
*   Explain when and why command-line interfaces should be used instead of graphical interfaces.

</div>

## An example:  Why use the shell?

Nelle Nemo, a marine biologist,
has just returned from a six-month survey of the
[North Pacific Gyre](http://en.wikipedia.org/wiki/North_Pacific_Gyre),
where she has been sampling gelatinous marine life in the
[Great Pacific Garbage Patch](http://en.wikipedia.org/wiki/Great_Pacific_Garbage_Patch).
She has 1520 samples in all, and now needs to:

1.  Run each sample through an assay machine
    that will measure the relative abundance of 300 different proteins.
    The machine's output for a single sample is
    a file with one line for each protein.
2.  Calculate statistics for each of the proteins separately
    using a program her supervisor wrote called `goostat`.
3.  Compare the statistics for each protein
    with corresponding statistics for each other protein
    using a program one of the other graduate students wrote called `goodiff`.
4.  Write up.
    Her supervisor would really like her to do this by the end of the month
    so that her paper can appear in an upcoming special issue of *Aquatic Goo Letters*.

It takes about half an hour for the assay machine to process each sample.
The good news is,
it only takes two minutes to set each one up.
Since her lab has eight assay machines that she can use in parallel,
this step will "only" take about two weeks.

The bad news is that if she has to run `goostat` and `goodiff` by hand,
she'll have to enter filenames and click "OK" 45,150 times
(300 runs of `goostat`, plus 300&times;299/2 runs of `goodiff`).
At 30 seconds each,
that will take more than two weeks.
Not only would she miss her paper deadline,
the chances of her typing all of those commands right are practically zero.

The next few lessons will explore what she should do instead.
More specifically,
they explain how she can use a command shell
to automate the repetitive steps in her processing pipeline
so that her computer can work 24 hours a day while she writes her paper.
As a bonus,
once she has put a processing pipeline together,
she will be able to use it again whenever she collects more data.

#### CLI vs GUI

At a high level, computers do four things:

-   run programs;
-   store data;
-   communicate with each other; and
-   interact with us.

Today, most of us use windows, icons, mice, and trackpads to interact with our computers.
These technologies didn't become widespread until the 1980s,
but their roots go back to the 1960s. Before that,
the only way to interact with early computers was to rewire them.
From the 1950s to the 1980s,
most people used line printers. Many of the commands and techniques we're going to learn about today date to this period.
Line printers only allowed input and output of the letters, numbers, and punctuation found on a standard keyboard, so programming languages and interfaces had to be designed around that constraint. This led to some particular design goals for shell  programs: 

The slow feedback of these early machines also meant that UNIX shell designers had some particular goals:

- minimize human errors: 
    - comands are terse
    - the shell can fill in blanks: tab completion, command expansion
    - command sequences are re-useable: scripting

- maximize effectiveness of each line:  
    - short commands that combine well
    - command history
    - scripting  

Today, most computers have two interfaces:   

- 'desktop environment' or GUI: a [graphical user interface](../../gloss.html#gui)
- 'shell' or  CLI: [command-line interface](../../gloss.html#cli)
Most people interact with their computers using the GUI.   

So let's explore some basic uses of the CLI. 

This is the origin of [ASCII text encoding](../../gloss.html#ascii). 

<div>
    <img src="./img/ASCII_Code_Chart-Quick_ref_card.jpg" alt="" width="60%">
</div>

Which led to ASCII art. 

#### What is the Shell?
The heart of a CLI is a [read-evaluate-print loop](../../gloss.html#repl), or REPL:
when the user types a command and then presses the enter (or return) key,
the computer reads it,
executes it,
and prints its output.
The user then types another command,
and so on until the user logs off.

This description makes it sound as though the user sends commands directly to the computer,
and the computer sends output directly to the user.
In fact,
there is usually a program in between called a
[command shell](../../gloss.html#shell).
What the user types goes into the shell;
it figures out what commands to run and orders the computer to execute them. 

A shell is a program like any other.
What's special about it is that its job is to run other programs
rather than to do calculations itself. Like the Finder program on a Mac or the KDE or Gnome programs on a Linux machine (often referred to as a 'Desktop environments'), it is often used to manage the file system. But the shell can do a lot more than that. 

The most popular Unix shell is Bash,
the Bourne Again SHell
(named because it a reworking of the Bourne shell, written by Stephen Bourne&mdash;this
is what passes for wit among programmers).
Bash is the default shell on most modern implementations of Unix,
and in most packages that provide Unix-like tools for Windows.

Using Bash or any other shell feels more like programming than like using a mouse.
Because Bash dates back to line printers, the commands are terse (often only a couple of characters long), their names are frequently cryptic,
and their output is lines of text rather than something visual like a graph.
On the other hand,
the shell is more configurable and flexible than a GUI. It allows us to combine existing tools in powerful ways with only a few keystrokes
and to set up pipelines to handle large volumes of data automatically.
The command line is also often the easiest way to interact with remote machines.
As clusters and cloud computing become more popular for scientific data crunching,
being able to drive them is becoming a necessary skill.

<div class="keypoints" markdown="1">

#### Key Points
*   A shell is a program whose primary purpose is to read commands and run other programs.
*   The shell's main advantages are its high action-to-keystroke ratio,
    its support for automating repetitive tasks,
    and that it can be used to access networked machines.
*   The shell's main disadvantages are its primarily textual nature
    and its cryptic commands. There's definitely a learning curve!

</div>
