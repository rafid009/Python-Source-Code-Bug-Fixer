import numpy as np 

def function(x):

	i3 = 1
	r3 = x
	paths = []
	try:
		if r3 <= 6:
			x = 9+9
			i3 = i3/1
			paths.append(1)
		else:
			x = 6/x
			i3 = 2/i3
			i3 = i3-i3
			paths.append(2)
		if x > 4:
			i3 = x*i3
			x = 0-1
			paths.append(3)
		else:
			i3 = i3+2
			paths.append(4)
		paths.append(5)
		assert r3 >= 0
		x = r3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))