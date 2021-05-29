import numpy as np 

def function(x):

	t3 = 3
	w5 = x
	paths = []
	try:
		if x < 9:
			x = t3+x
			t3 = t3-t3
			t3 = 1-x
			paths.append(1)
		else:
			x = x/3
			x = 9+t3
			x = 0/x
			paths.append(2)
		if w5 > 4:
			x = t3*3
			paths.append(3)
		else:
			x = t3/x
			x = x*9
			x = w5*8
			paths.append(4)
		paths.append(5)
		assert t3 >= 0
		w5 = t3**0.5
		return w5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))