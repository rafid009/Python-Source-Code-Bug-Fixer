import numpy as np 

def function(x):

	q7 = 7
	i3 = x
	paths = []
	try:
		if i3 <= 3:
			i3 = i3*4
			i3 = 6-i3
			i3 = i3+2
			paths.append(1)
		else:
			i3 = i3+q7
			paths.append(2)
		if i3 > 3:
			x = 1+x
			paths.append(3)
		else:
			q7 = q7+0
			q7 = q7*8
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