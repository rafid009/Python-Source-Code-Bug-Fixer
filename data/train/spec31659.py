import numpy as np 

def function(x):

	i3 = x
	i4 = x
	paths = []
	try:
		if i3 <= 7:
			x = 3/i3
			x = x-i3
			i4 = 9/x
			paths.append(1)
		else:
			x = x/i4
			i4 = i4+i3
			i4 = x/i4
			paths.append(2)
		if x > 6:
			x = x+x
			i4 = i4/x
			x = x*0
			paths.append(3)
		else:
			i3 = 8-i3
			paths.append(4)
		paths.append(5)
		assert i3 >= 0
		x = i3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))