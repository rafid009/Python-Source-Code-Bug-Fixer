import numpy as np 

def function(x):

	g9 = x
	i5 = 3
	paths = []
	try:
		if i5 <= 4:
			i5 = i5+g9
			i5 = i5-9
			x = 1+7
			paths.append(1)
		else:
			x = x+7
			x = 7/x
			paths.append(2)
		if x > 5:
			x = 6+3
			g9 = g9-g9
			g9 = g9-2
			paths.append(3)
		else:
			g9 = x/3
			paths.append(4)
		paths.append(5)
		assert g9 >= 0
		i5 = g9**0.5
		return i5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))