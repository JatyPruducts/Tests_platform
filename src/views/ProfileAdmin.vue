<template>
    <header>
        <div class="offcanvas offcanvas-start"  tabindex="-1" id="Sections" aria-labelledby="SectionsLabel">
        <div class="offcanvas-header">
            <h5 class="offcanvas-title" id="SectionsLabel">Оглавление</h5>
            <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
        </div>
        <div class="offcanvas-body">
            <p>Lorem ipsum odor amet, consectetuer adipiscing elit. Mollis posuere sociosqu rhoncus rutrum suscipit pulvinar praesent eu. Congue bibendum parturient commodo ad parturient imperdiet vel etiam auctor. Purus sed nisi platea massa vivamus magnis vehicula varius. Porta ante ullamcorper vel eleifend proin amet quisque. Nascetur porttitor semper aliquet platea viverra inceptos. Eu diam molestie euismod justo vel aptent pulvinar rutrum. Consectetur facilisis pellentesque dapibus adipiscing consectetur conubia. Quis magnis luctus nostra nec litora; potenti mi tempus. Pharetra commodo malesuada ad nisl mattis, sodales integer dictumst. Cursus dictum pellentesque; id finibus neque ac tempor placerat felis. Sagittis vel lorem; urna rhoncus arcu vestibulum. Condimentum sem tristique; eu suscipit lectus sapien. Diam elementum adipiscing leo; ultrices id ut. Orci himenaeos morbi augue bibendum venenatis morbi senectus condimentum. Tristique leo tristique lobortis litora magna eros varius? Commodo dictumst blandit tortor mauris nisi rutrum pulvinar. Lacus nisl sociosqu orci mattis class luctus. Leo condimentum suscipit ornare habitasse maximus penatibus urna. Integer parturient eleifend suspendisse etiam metus risus eget convallis. Phasellus viverra sit sollicitudin ex pulvinar donec platea vestibulum proin. Non tortor neque enim, aliquam urna per varius. Blandit fermentum habitasse faucibus quis nulla potenti dolor. Vitae interdum tempor senectus sapien cubilia leo class hendrerit? Enim libero turpis sociosqu diam mattis iaculis. Semper primis tellus libero torquent primis aliquam nullam nisl etiam. Habitasse augue litora habitasse quam molestie et enim. Malesuada bibendum convallis leo leo congue. Sociosqu suscipit turpis integer inceptos commodo velit iaculis montes eros. Hac massa viverra diam sed ridiculus egestas platea. Dolor sem nam imperdiet tortor odio. Aligula nascetur lobortis lobortis eu justo metus. Aptent purus viverra massa non amet nisi rutrum libero tristique? Hac parturient efficitur ante amet sit pellentesque nulla tincidunt. Sem integer litora vitae semper per maximus. Ipsum habitasse suscipit dolor mauris elementum. Hac imperdiet taciti himenaeos pellentesque, imperdiet torquent.</p> <br>
        </div>
        </div>
        <b-navbar toggleable="lg" type="dark" class="bg-info bg-gradient shadow">
            <div>
                <button type="button" class="btn border rounded p-2" data-bs-toggle="offcanvas" data-bs-target="#Sections" aria-controls="Sections" style="background-color: yellow; color: black;">
                    <i class="bi bi-list"> Разделы</i>
                </button>
            </div>
                <b-nav-item-dropdown class="border rounded p-2" style="background-color: yellow;font-size: large;" right>
                    <template #button-content>
                        <i class='bi bi-person-square'></i> 
                         <em> Имя</em> <!--заменим на Имя из БД -->
                    </template>
                    <b-dropdown-item href="#">Статистика</b-dropdown-item>
                    <b-dropdown-item href="#">Учителя</b-dropdown-item>
                    <b-dropdown-item href="#">Ученики</b-dropdown-item>
                    <b-dropdown-item href="#">Пользователи</b-dropdown-item>
                </b-nav-item-dropdown>
        </b-navbar>
    </header>
    <body>
        <b-card>
            <b-card-body style="position:relative; height:85vh; overflow-y:scroll; text-align: left;">
                <p>{{ text }}</p>
            </b-card-body>
        </b-card>
    </body>
</template>

<script>

export default {
    name: 'ProfileAdmin',
    data() {
      return {
        text: "Lorem ipsum odor amet, consectetuer adipiscing elit. Mollis posuere sociosqu rhoncus rutrum suscipit pulvinar praesent eu. Congue bibendum parturient commodo ad parturient imperdiet vel etiam auctor. Purus sed nisi platea massa vivamus magnis vehicula varius. Porta ante ullamcorper vel eleifend proin amet quisque. Nascetur porttitor semper aliquet platea viverra inceptos. Eu diam molestie euismod justo vel aptent pulvinar rutrum. Consectetur facilisis pellentesque dapibus adipiscing consectetur conubia. Quis magnis luctus nostra nec litora; potenti mi tempus. Pharetra commodo malesuada ad nisl mattis, sodales integer dictumst. Cursus dictum pellentesque; id finibus neque ac tempor placerat felis. Sagittis vel lorem; urna rhoncus arcu vestibulum. Condimentum sem tristique; eu suscipit lectus sapien. Diam elementum adipiscing leo; ultrices id ut. Orci himenaeos morbi augue bibendum venenatis morbi senectus condimentum. Tristique leo tristique lobortis litora magna eros varius? Commodo dictumst blandit tortor mauris nisi rutrum pulvinar. Lacus nisl sociosqu orci mattis class luctus. Leo condimentum suscipit ornare habitasse maximus penatibus urna. Integer parturient eleifend suspendisse etiam metus risus eget convallis. Phasellus viverra sit sollicitudin ex pulvinar donec platea vestibulum proin. Non tortor neque enim, aliquam urna per varius. Blandit fermentum habitasse faucibus quis nulla potenti dolor. Vitae interdum tempor senectus sapien cubilia leo class hendrerit? Enim libero turpis sociosqu diam mattis iaculis. Semper primis tellus libero torquent primis aliquam nullam nisl etiam. Habitasse augue litora habitasse quam molestie et enim. Malesuada bibendum convallis leo leo congue. Sociosqu suscipit turpis integer inceptos commodo velit iaculis montes eros. Hac massa viverra diam sed ridiculus egestas platea. Dolor sem nam imperdiet tortor odio. Aligula nascetur lobortis lobortis eu justo metus. Aptent purus viverra massa non amet nisi rutrum libero tristique? Hac parturient efficitur ante amet sit pellentesque nulla tincidunt. Sem integer litora vitae semper per maximus. Ipsum habitasse suscipit dolor mauris elementum. Hac imperdiet taciti himenaeos pellentesque, imperdiet torquent. Vivamus tempor imperdiet ultricies maximus rutrum."
        }
    }
}
</script>