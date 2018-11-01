import pandas as pd

playing_pos_data = pd.read_csv("PlayerPlayingPositionData.csv")
player_personal_data = pd.read_csv("PlayerPersonalData.csv")
Player_attributes = pd.read_csv("PlayerAttributeData.csv")

Player_attributes = Player_attributes[Player_attributes.columns.values].apply(pd.to_numeric, errors="coerce")

total_player_data = player_personal_data.drop(['Unnamed: 0'],axis=1)
# total_player_data = total_player_data.drop(["Unnamed: 0.1"], axis=1)
total_player_data = total_player_data.drop(["Unnamed: 0.1","Photo",
                                            "Flag", "Club Logo"],
                                           axis=1)

total_player_data["playing position"] = playing_pos_data["Preferred Positions"]
Player_attributes = Player_attributes.drop(["Unnamed: 0"], axis=1)

total_player_data[Player_attributes.columns.values] = Player_attributes[Player_attributes.columns.values]

goalKeepers = pd.DataFrame([])

for i in range(0, len(total_player_data)):
    if total_player_data["playing position"][i] == "GK ":
        goalKeepers = goalKeepers.append(total_player_data[i:i+1])

# nongoalKeepers = pd.DataFrame([])
#
# for i in range(0, len(total_player_data)):
#     if total_player_data["playing position"][i] != "GK ":
#         nongoalKeepers = nongoalKeepers.append(total_player_data["GK diving"][i:i+1])


goalKeepers = goalKeepers.reset_index()

# frame = pd.DataFrame([])
def create_frame(name1):
    data = pd.DataFrame([])
    # data = data.append(goalKeepers[goalKeepers["Name"] == name1])
    # data = data.append(goalKeepers[goalKeepers["Name"] == name2])
    # data = data.append(goalKeepers[goalKeepers["Name"] == name3])
    data = data.append(total_player_data[total_player_data["Name"] == name1])
    # data = data.append(total_player_data[total_player_data["Name"] == name2])
    # data = data.append(total_player_data[total_player_data["Name"] == name3])
    return data



# frame = create_frame("M. Neuer", "B. Leno", "J. Oblak")


# Libraries
import matplotlib.pyplot as plt
import pandas as pd
from math import pi

# Set data
# df = pd.DataFrame({
#     'group': ['A', 'B', 'C', 'D'],
#     'diving': [38, 1.5, 30, 4],
#     'kicking': [29, 10, 9, 34],
#     'a': [8, 39, 23, 24],
#     'var4': [7, 31, 33, 14],
#     'var5': [28, 15, 32, 14],
#     'var6': [28, 15, 32, 14]
# })
# df = frame[["Name", "Overall", "GK diving", "GK handling", "GK positioning",
#             "GK kicking", "GK reflexes", "Jumping"]]





from Tkinter import *
# import mpld3
# import Tkinter
#
# top = Tkinter.Tk()
#
# button1 = Tkinter.Button(master=top, text="Compare!",
#                          height=3, width=20,
#                          activebackground="#000000",  # color of button when clicked
#                          activeforeground="#ffffff",  # color of text
#                          bg="#777777", bd=1)  # background and border
# button1.pack()
# # l = Label(win, text="This is a label")
# # l.grid(row=1,column=0)
#
# window = top.mainlo


win = Tk()


lb1 = Listbox(win, height=20)
# lb2 = Listbox(win, height=6)

names = total_player_data.Name

def fill_list(names_list):
    for i in range(0,len(names_list)):
        lb1.insert(END, names_list[i])
        # lb2.insert(END, names_list[i])


fill_list(names_list=names)


sb1 = Scrollbar(win,orient=VERTICAL)
# sb2 = Scrollbar(win,orient=VERTICAL)
lb1.configure(yscrollcommand=sb1.set)
# lb2.configure(yscrollcommand=sb2.set)
fig = plt.figure(figsize=(8,8))

# sb1.pack(side=RIGHT)
label1 = Label(win, text="Player Names")
label1.pack()
lb1.pack(padx=60, pady=10)
# sb2.pack(side=RIGHT)
# label2 = Label(win, text="Player 2 :")
# label2.pack()
# lb2.pack(padx=10)
b1 = Button(win, text="Plot this Player!")
b1.pack(padx=10, pady=10)
b2 = Button(win, text="Clear figure")
b2.pack(padx=10, pady=10)

def button():
    player = lb1.get(lb1.curselection())
    print player

    frame = create_frame(player)
    frame = frame.reset_index()
    df = frame[["Name", "Vision", "Interceptions", "Crossing", "Dribbling",
                "Balance", "Free kick accuracy", "Marking", "Positioning",
                "Ball control", "Finishing", "GK diving", "GK reflexes", "Acceleration"]]
    def radar_plot(dataframe):
        # number of variable
        categories = list(dataframe)[1:]
        N = len(categories)

        # We are going to plot the first line of the data frame.
        # But we need to repeat the first value to close the circular graph:
        # values = dataframe.loc[0].drop('group').values.flatten().tolist()
        # values += values[:1]
        # values

        # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
        angles = [n / float(N) * 2 * pi for n in range(N)]
        angles += angles[:1]

        # Initialise the spider plot
        # fig = plt.figure(figsize=(10,10))
        ax = fig.add_subplot(111, polar=True, facecolor="whitesmoke")


        # Draw one axe per variable + add labels labels yet
        plt.xticks(angles[:-1], categories, color='grey', size=8)

        # Draw ylabels
        ax.set_rlabel_position(0)
        plt.yticks([25, 50, 75], ["25", "50", "75"], color="grey", size=7)
        plt.ylim(0, 100)

        # # Plot data
        # ax.plot(angles, values, linewidth=1, linestyle='solid')
        #
        # # Fill area
        # ax.fill(angles, values, 'b', alpha=0.1)

        # ------- PART 2: Add plots

        # Plot each individual = each line of the data
        # I don't do a loop, because plotting more than 3 groups makes the chart unreadable

        # Ind1
        values = df.loc[0].drop('Name').values.flatten().tolist()
        # print values
        values += values[:1]
        ax.plot(angles, values, linewidth=2, linestyle='solid', label=dataframe.Name[0])
        ax.fill(angles, values, 'b', alpha=0.1)

        # Ind2
        # values = df.loc[1].drop('Name').values.flatten().tolist()
        # values += values[:1]
        # ax.plot(angles, values, linewidth=3, linestyle='solid', label=dataframe.Name[1])
        # ax.fill(angles, values, 'r', alpha=0.1)

        # Ind3
        # values = df.loc[2].drop('Name').values.flatten().tolist()
        # values += values[:1]
        # ax.plot(angles, values, linewidth=3, linestyle='solid', label=dataframe.Name[2])
        # ax.fill(angles, values, 'g', alpha=0.1)

        # Add legend
        plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

        #save file
        plt.savefig("radar_plot.png")
        # plt.connect("motion_notify_event")

        # def on_plot_hover(event):
        #     for curve in ax.get_lines():
        #         if curve.contains(event)[0]:
        #             print "over %s" % curve.get_gid()
        #
        # fig.canvas.mpl_connect('motion_notify_event', on_plot_hover)

        # tooltip = mpld3.plugins.PointLabelTooltip(ax, labels=labels)
        # mpld3.plugins.connect(fig, tooltip)
        tooltip = ax.annotate("X", xy=(1,2))
        tooltip.set_visible(False)

        def on_move(event):
            if event.inaxes is not None:
                y = int(event.ydata)
                print y
                tooltip = ax.annotate(y, xy=(event.xdata, event.ydata),
                                      bbox=dict(boxstyle="round", fc="w"),
                                      arrowprops=dict(arrowstyle="->"))
                tooltip.get_bbox_patch().set_facecolor("#cccccc")
                tooltip.set_visible(True)

                fig.canvas.draw_idle()

        def clear_tooltip(event):
                tooltip.set_visible(False)
                fig.canvas.draw_idle()
        # plt.connect("motion_notify_event", on_move)
        # plt.connect("axes_leave_event", clear_tooltip)

    radar_plot(df)
    pos_label = Label(win, text=frame["playing position"].values[0], background="#cccccc")
    pos_label.pack()


def clear():
    fig.clf()
    # print win.pack_slaves()
    elements = win.pack_slaves()
    for i in range(4,len(elements)):
        elements[i].destroy()


b1.configure(command=button)
b2.configure(command=clear)

# lb.curselection()
win.mainloop()
