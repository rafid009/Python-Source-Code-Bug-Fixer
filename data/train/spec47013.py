import numpy as np 

def function(x):

	f6 = 9
	t5 = x
	x = x
	paths = []
	try:
		if t5 >= 7:
			t5 = 1+f6
			paths.append(1)
		else:
			f6 = x+t5
			x = 9/x
			paths.append(2)
		if f6 < 5:
			x = x/4
			paths.append(3)
		else:
			f6 = f6*t5
			f6 = 0/x
			t5 = 3+t5
			paths.append(4)
		paths.append(5)
		assert t5 >= 0
		t5 = t5**0.5
		return t5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))