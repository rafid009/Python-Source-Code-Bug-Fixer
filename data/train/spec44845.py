import numpy as np 

def function(x):

	g5 = x
	i3 = 5
	paths = []
	try:
		if i3 < 1:
			g5 = 5+g5
			x = x*i3
			paths.append(1)
		else:
			g5 = g5*g5
			i3 = 2*i3
			paths.append(2)
		if g5 < 7:
			i3 = i3/7
			g5 = x/9
			i3 = i3*8
			paths.append(3)
		else:
			i3 = 7*2
			i3 = 4/3
			paths.append(4)
		paths.append(5)
		assert g5 >= 0
		i3 = g5**0.5
		return i3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))