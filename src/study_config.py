STUDY_PROBLEMS = [
    {
        "id": 0,
        "candidates": [
            # "(F r) & (r -> (X(G (!r))))",
            # "F (r & X (G (!r)))",
            # "(! r) U (r & (G(! r)))",
            # "F (r) & (r -> X (G !r))",
            "(!r) U (r & X(G(!r)))",
            # "F (r & X (G (! r)))",
            "F(X(r))",
            "G(F(r) -> X(G(!r))) & F(r)",
            "F(r & X(G(!r)))",
            "G (r -> XG!r)",
            "F(r) & (r -> X(G(!r)))",
            # "F(r) & !(F(r & F(r)))",
            # "F(r & X(G(!r)))",
            "F(r)",
            "X(F(r) U G(!r))",
            "(F(r) -> G(!r))",
            # "X(F(r))",
        ],
        "description": """There is an instrument panel with three colors: Red, Green, and Blue. <b>Red is on in exactly one state, not necessarily the first.</b> The variable <code>r</code> indicates when the red light is on, the variable <code>g</code>  when the green light is on, and the variable <code>b</code> when the blue light is on.""",
        "correct": "(!r) U (r & X(G(!r)))",
    },
    {
        "id": 1,
        "candidates": [
            "(r U !r) & (G(!r -> G(!r)))",
            # "F (! r & G ! r)",
            "r U (! r) & (!r -> X !r)",
            "r ->(X(r) | (G !(r)))",
            # "r U (F (G (!r)))",
            "F(G(!r))",
            "F(r -> X(G(!r)))",
            # "FG(!r)",
            "G(r) U G(!r)",
            # "G(F(r)) U (G(!r))",
            "F(r) & G(r -> X(U(!r)))",
        ],
        "description": """There is an instrument panel with three colors: Red, Green, and Blue. <b>The Red light is on for zero or more states, and then turns off and remains off in the future.</b> The variable <code>r</code> indicates when the red light is on, the variable <code>g</code>  when the green light is on, and the variable <code>b</code> when the blue light is on.""",
        "correct": "(r U !r) & (G(!r -> G(!r)))",
    },
    {
        "id": 2,
        "candidates": [
            "G(X(r) -> (X(b) | F(b)))",
            "G(r -> F(b))",
            "r -> (F(b))",
        ],
        "description": """There is an instrument panel with three colors: Red, Green, and Blue. <b>Whenever the Red light is on, the Blue light will be on then or at some point in the future.</b> The variable <code>r</code> indicates when the red light is on, the variable <code>g</code>  when the green light is on, and the variable <code>b</code> when the blue light is on.""",
        "correct": "G(r -> F(b))",
    },
    
]

STUDY_VERSION = 3
SHOW_CANDIDATES = False
SHOW_LABELS = False
CONFIDENCE_THRESHOLD = 4
UNSURE_THRESHOLD = 6
ELIMINATION_THRESHOLD = 2
TESTING = True