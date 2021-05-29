import numpy as np 

def function(x):

	t8 = x
	w9 = 0
	paths = []
	try:
		if w9 > 8:
			t8 = t8*0
			t8 = 6-t8
			t8 = 3*t8
			paths.append(1)
		else:
			t8 = t8/9
			t8 = x-0
			w9 = x+w9
			paths.append(2)
		if t8 <= 3:
			x = t8/w9
			paths.append(3)
		else:
			w9 = w9*7
			paths.append(4)
		paths.append(5)
		assert w9 >= 0
		w9 = w9**0.5
		return w9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))