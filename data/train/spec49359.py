import numpy as np 

def function(x):

	w6 = 9
	t7 = 9
	paths = []
	try:
		if x >= 0:
			x = t7*0
			w6 = w6+x
			t7 = t7*9
			paths.append(1)
		else:
			x = x-t7
			w6 = w6*6
			paths.append(2)
		if x <= 6:
			w6 = t7+x
			t7 = 7*w6
			w6 = x+w6
			paths.append(3)
		else:
			t7 = 8+t7
			paths.append(4)
		paths.append(5)
		assert w6 >= 0
		w6 = w6**0.5
		return w6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))