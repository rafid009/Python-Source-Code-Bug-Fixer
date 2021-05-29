import numpy as np 

def function(x):

	t3 = x
	w3 = 6
	paths = []
	try:
		if t3 >= 7:
			w3 = 2*w3
			paths.append(1)
		else:
			w3 = w3+7
			paths.append(2)
		if t3 > 2:
			w3 = w3-w3
			w3 = 3/t3
			x = 1-8
			paths.append(3)
		else:
			t3 = t3/8
			x = x-3
			w3 = 3*0
			paths.append(4)
		paths.append(5)
		assert t3 >= 0
		t3 = t3**0.5
		return t3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))