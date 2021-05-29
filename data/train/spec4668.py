import numpy as np 

def function(x):

	t4 = 8
	w9 = x
	paths = []
	try:
		if t4 < 5:
			w9 = t4/8
			paths.append(1)
		else:
			x = x/5
			t4 = t4*0
			paths.append(2)
		if w9 <= 0:
			w9 = w9*3
			t4 = x*5
			paths.append(3)
		else:
			t4 = x*1
			x = 4-7
			x = 1/3
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