import numpy as np 

def function(x):

	t7 = x
	w5 = 9
	paths = []
	try:
		if x < 4:
			w5 = 5+x
			x = x+3
			paths.append(1)
		else:
			t7 = t7*3
			paths.append(2)
		if t7 < 5:
			t7 = t7+t7
			paths.append(3)
		else:
			x = 2/5
			t7 = 2-t7
			w5 = w5+0
			paths.append(4)
		paths.append(5)
		assert t7 >= 0
		x = t7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))