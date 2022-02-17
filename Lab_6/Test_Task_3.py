from Task_3 import *


def testShowWomenScientist():
    curie = womenScientists("Mare Curie", "Warsaw", "Poland", 1867)
    franklin = womenScientists(
        "Rosalind Franklin", "Notting Hill", "United Kingdom", 1920)
    meitner = womenScientists("Lise Meitner", "Vienna", "Austria", 1879)
    lovelace = womenScientists(
        "Ada Lovelace", "London", "United Kingdom", 1815)
    ball = womenScientists("Alice Ball", "Seattle", "Washington", 1892)
    wu = womenScientists("Chien-Shiung Wu", "Suzhou", "China", 1912)
    curie.addAchievement("pioneered research on radioactivity.")
    franklin.addAchievement(
        "used a technique called X-ray crystallography, and revealed the helical shape of the DNA molecule.")
    meitner.addAchievement(
        "was one of those responsible for the discovery of the element protactinium and nuclear fission.")
    lovelace.addAchievement(
        "was known for her work on Charles Babbage's proposed mechanical general-purpose computer, the Analytical Engine.")
    ball.addAchievement(
        "developed the Ball Method, the most effective treatment for leprosy during the early 20th century.")
    wu.addAchievement(
        "worked on the Manhattan Project, where she helped develop the process for separating uranium into uranium-235 and uranium-238 isotopes by gaseous diffusion.")

    womenScientists.makeGreat()

    assert womenScientists.showWomenScientists(test=True) == ["The Great M Curie pioneered research on radioactivity.",
                                                              "The Great R Franklin used a technique called X-ray crystallography, and revealed the helical shape of the DNA molecule.",
                                                              "The Great L Meitner was one of those responsible for the discovery of the element protactinium and nuclear fission.",
                                                              "The Great A Lovelace was known for her work on Charles Babbage's proposed mechanical general-purpose computer, the Analytical Engine.",
                                                              "The Great A Ball developed the Ball Method, the most effective treatment for leprosy during the early 20th century.",
                                                              "The Great C Wu worked on the Manhattan Project, where she helped develop the process for separating uranium into uranium-235 and uranium-238 isotopes by gaseous diffusion."]


testShowWomenScientist()
print("Pass")
