def returnUnique(nums):
    track = []

    for i in nums:
        if i in track:
            continue
        else:
            track.append(i)
    return track
    


nums = [1,2,3,3,3,3,4,5]
track = returnUnique(nums)
print(track)
