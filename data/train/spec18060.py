import numpy as np 

def function(x):

	u5 = x
	i3 = x
	paths = []
	try:
		if u5 >= 9:
			i3 = 7-4
			i3 = i3*2
			paths.append(1)
		else:
			u5 = 8/u5
			i3 = i3-7
			x = 5/i3
			paths.append(2)
		if i3 < 9:
			i3 = i3/x
			paths.append(3)
		else:
			x = x-9
			u5 = 8*4
			u5 = u5/6
			paths.append(4)
		paths.append(5)
		assert u5 >= 0
		u5 = u5**0.5
		return u5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))