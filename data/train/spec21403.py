import numpy as np 

def function(x):

	t3 = x
	w5 = 9
	paths = []
	try:
		if x < 3:
			x = 7+2
			paths.append(1)
		else:
			x = x/7
			w5 = w5/w5
			w5 = w5-4
			paths.append(2)
		if t3 < 7:
			x = 3/x
			w5 = w5/4
			w5 = w5/9
			paths.append(3)
		else:
			t3 = t3/9
			x = t3+t3
			w5 = w5/6
			paths.append(4)
		paths.append(5)
		assert w5 >= 0
		t3 = w5**0.5
		return t3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))