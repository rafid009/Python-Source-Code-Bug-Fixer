import numpy as np 

def function(x):

	t6 = x
	w7 = 1
	paths = []
	try:
		if x >= 8:
			x = x*0
			paths.append(1)
		else:
			t6 = t6+x
			paths.append(2)
		if x < 9:
			t6 = w7+t6
			t6 = 3-t6
			paths.append(3)
		else:
			t6 = t6/9
			w7 = t6/w7
			w7 = 0/1
			paths.append(4)
		paths.append(5)
		assert t6 >= 0
		w7 = t6**0.5
		return w7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))