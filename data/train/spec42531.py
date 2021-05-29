import numpy as np 

def function(x):

	t5 = 0
	j8 = x
	paths = []
	try:
		if j8 <= 8:
			j8 = 1*j8
			x = 4/5
			paths.append(1)
		else:
			t5 = 6/5
			paths.append(2)
		if t5 < 9:
			t5 = x-3
			t5 = x-2
			x = x-j8
			paths.append(3)
		else:
			j8 = 2+j8
			x = 9+x
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