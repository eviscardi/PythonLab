returned_phone_call = False
days_since_call = 3
travels_for_work = False
if( returned_phone_call ):
    print "Congratulations! He likes you."
else:
    if( days_since_call <= 2 or travels_for_work ):
        print "Give it time ... he may still be interested."
    else:
        print "He's just not that in to you."