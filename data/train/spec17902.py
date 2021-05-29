import numpy as np 

def function(x):

	o2 = x
	g8 = x
	paths = []
	try:
		if g8 <= 8:
			x = o2-o2
			paths.append(1)
		else:
			x = x+7
			x = x*1
			paths.append(2)
		if g8 < 5:
			x = 3+o2
			g8 = g8*1
			o2 = o2/9
			paths.append(3)
		else:
			o2 = 0+o2
			o2 = o2+g8
			paths.append(4)
		paths.append(5)
		assert g8 >= 0
		o2 = g8**0.5
		return o2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))