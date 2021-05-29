import numpy as np 

def function(x):

	t1 = x
	w1 = x
	paths = []
	try:
		if t1 <= 9:
			x = 5*x
			w1 = 9+w1
			w1 = w1+2
			paths.append(1)
		else:
			t1 = 6+t1
			t1 = t1+w1
			t1 = t1-1
			paths.append(2)
		if t1 >= 3:
			w1 = w1+x
			t1 = 0/t1
			w1 = w1*w1
			paths.append(3)
		else:
			w1 = 7+w1
			x = x+5
			paths.append(4)
		paths.append(5)
		assert t1 >= 0
		t1 = t1**0.5
		return t1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))