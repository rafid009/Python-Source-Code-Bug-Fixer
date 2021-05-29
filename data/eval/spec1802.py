import numpy as np 

def function(x):

	a7 = 2
	i3 = 4
	paths = []
	try:
		if x > 1:
			x = x-8
			i3 = 6/i3
			i3 = a7-i3
			paths.append(1)
		else:
			a7 = 2+a7
			i3 = i3+i3
			a7 = 5*0
			paths.append(2)
		if a7 < 3:
			a7 = a7+4
			i3 = 3-i3
			paths.append(3)
		else:
			i3 = x-x
			x = 7*0
			a7 = i3/9
			paths.append(4)
		paths.append(5)
		assert i3 >= 0
		a7 = i3**0.5
		return a7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))