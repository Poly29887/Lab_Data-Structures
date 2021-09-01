bidder_list = [int(i) for i in input("Enter All Bid : ").split()]
if len(bidder_list)<=1:
    print('not enough bidder')
else :
    bidder_list.sort(reverse=True)
    if bidder_list[0]==bidder_list[1]:
        print('error : have more than one highest bid')
    else :
        print('winner bid is {} need to pay {}'.format(bidder_list[0],bidder_list[1]))
