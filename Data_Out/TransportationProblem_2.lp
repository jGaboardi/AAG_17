\ Model TransportationProblem_2
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  9 sd[0,0] + 9 sd[0,1] + 7 sd[1,0] + 3 sd[1,1]
Subject To
 Supply[0]: sd[0,0] + sd[0,1] <= 85
 Supply[1]: sd[1,0] + sd[1,1] <= 114
 Demand[0]: sd[0,0] + sd[1,0] >= 17
 Demand[1]: sd[0,1] + sd[1,1] >= 44
Bounds
End
