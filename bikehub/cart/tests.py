from django.test import TestCase

# Create your tests here.


# @login_required(login_url='/admin/login/')
# def add_to_cart(request, id=None):
#     carts = Cart.objects.all()
#     if request.method == 'POST':
#         form = CartForm(request.POST)
#         if form.is_valid():
#             print("form valid")
#             form.save(commit=False)
#             form.user = request.user
#             form.date = timezone.now()
#             form.save()
#             messages.success(
#                 request, 'You have successfully added your items in cartbox')
#         else:
#             messages.error(request, 'Error adding items in cartbox')

#     instance = get_object_or_404(Cart, id=id)
#     if request.method == 'GET':
#         form = CartForm(request.GET or None,
#                         request.FILES or None, instance=instance)
#         if form.is_valid():
#             instance.delete()
#             messages.success(
#                 request, 'You have successfully deleted the selected cart')
#         else:
#             messages.error(
#                 request, 'You have failed deleting the previously selected cart')
#     context = {
#         "carts": carts,
#         "instance": instance,
#         "form": form
#     }
#     return render(request, 'cart/add_to_cart.html', context)


# <div class = "container mt-4" >
#     <div class = "row" >
#         {% for bike in bike_list % }
#         <div class = "col-xs-12 col-md-4" >
#             <div class = "bike" >
#                <div >
#                     <img src = "{{bike.image.url}}" alt = "{{bike.name}}" class = "myimage" >
#                 </div >
#                 <div class = "card-body">
#                     {{bike.name}} < br>
#                     Price:{{bike.price}} < br>
#                     <form action = "{% url 'cart:add_to_cart' %}" method="POST">
#                         { % csrf_token % }
#                         <button class = "btn btn-secondary" id="name" value="{{bike.id}}" name="bike_id" type="submit"><a
#                                 href = "" class="sobit">Add
#                                 to
#                                 cart < /a></button>
#                         <button class = "btn btn-secondary" id="name" value="{{bike.id}}" name="bike_id" type="submit"><a
#                                 href = "{% url '' %}" class="sobit">Preview</a></button>
#                     </form >
#                 </div >
#             </div >
#         </div >
#         { % endfor % }
#     </div >
# </div >
