import numpy as np 

def function(x):

	t5 = 0
	w6 = x
	paths = []
	try:
		if w6 <= 0:
			t5 = 9/w6
			paths.append(1)
		else:
			x = x-7
			t5 = t5+8
			paths.append(2)
		if t5 > 5:
			t5 = t5+t5
			x = x+t5
			t5 = t5/t5
			paths.append(3)
		else:
			t5 = t5*1
			paths.append(4)
		paths.append(5)
		assert w6 >= 0
		t5 = w6**0.5
		return t5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))