import sys

sys.path.append("../")
from pycore.blocks import *
from pycore.tikzeng import *


# https://github.com/HarisIqbal88/PlotNeuralNet/pull/120/files
# FullCon
def to_FulCon(
    name,
    s_filer=256,
    n_filer=64,
    offset="(0,0,0)",
    to="(0,0,0)",
    width=1,
    height=40,
    depth=40,
    caption=" ",
):
    return (
        r"""
\pic[shift={"""
        + offset
        + """}] at """
        + to
        + """ 
    {Box={
        name="""
        + name
        + """,
        caption="""
        + caption
        + r""",
        xlabel={{"""
        + str(n_filer)
        + """, }},
        zlabel="""
        + str(s_filer)
        + """,
        fill=\FcColor,
        height="""
        + str(height)
        + """,
        width="""
        + str(width)
        + """,
        depth="""
        + str(depth)
        + """
        }
    };
"""
    )


arch = [
    to_head(".."),
    to_cor(),
    to_begin(),
    to_FulCon(
        "fc1",
        2,
        1,
        offset="(0,0,0)",
        height=3,
        depth=10,
        width=3,
        caption="FC1",
    ),
    to_FulCon(
        "fc2",
        12,
        1,
        offset="(3,0,0)",
        height=3,
        depth=60,
        width=3,
        caption="FC2",
    ),
    to_FulCon(
        "fc3",
        4,
        1,
        offset="(6,0,0)",
        # to="(fc1-east)",
        height=3,
        depth=20,
        width=3,
        caption="FC3",
    ),
    to_FulCon(
        "output",
        1,
        1,
        offset="(9,0,0)",
        # to="(fc1-east)",
        height=3,
        depth=5,
        width=3,
        caption="Output",
    ),
    to_connection("fc1", "fc2"),
    to_connection("fc2", "fc3"),
    to_connection("fc3", "output"),
    to_end(),
]


def main():
    namefile = str(sys.argv[0]).split(".")[0]
    to_generate(arch, namefile + ".tex")


if __name__ == "__main__":
    main()
